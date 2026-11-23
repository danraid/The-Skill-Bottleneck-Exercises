#!/usr/bin/env python3
import json,re,shutil,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BOOK=ROOT/"_book"
LAB_MAP={"01":["01"],"02":["02"],"03":["03"],"04":["12"],"05":["02"],"06":["03","04"],"07":["04","05"],"08":["06"],"09":["06"],"10":["07"],"11":["09"],"12":["08"],"13":["10"],"14":["14"],"15":["11","12"],"16":["11","12"],"17":["13"],"18":["14"],"19":["13","14"],"20":["09","14"]}
STOP=set("the and for of with from into between what which when why how where are has have can does agent agents skill skills system systems using this that should".split())
def cleaned(s):
    s=re.sub(r"\[(?:doi:|title:)[^\]]+\]","",s)
    s=re.sub(r"[*_#]","",s)
    return re.sub(r"\s+"," ",s).strip()
def words(s):
    return set(w for w in re.findall(r"[a-z0-9-]+",cleaned(s).lower()) if len(w)>2 and w not in STOP)
def sections(s):
    p=re.split(r"(?m)^## +(.+?)\s*$",s)
    return [(p[i],p[i+1]) for i in range(1,len(p)-1,2)]
def items(s):
    markers=list(re.finditer(r"(?m)^\s*(\d{1,2})\.\s+",s))
    if markers:
        result=[]
        for i,m in enumerate(markers):
            end=markers[i+1].start() if i+1<len(markers) else len(s)
            t=cleaned(s[m.end():end])
            if len(t)>12:result.append(t[:1800])
        return result[:20]
    return [cleaned(x)[:1800] for x in re.split(r"(?m)^### +",s)[1:] if len(cleaned(x))>12][:20]
def evidence(q,paras):
    tokens=words(q)
    ranked=sorted(paras,key=lambda s:len(tokens&words(s))/(1+len(words(s))**0.3),reverse=True)
    found=[]
    for p in ranked[:3]:
        sentences=re.split(r"(?<=[.!?])\s+",p)
        sentences.sort(key=lambda x:-len(tokens&words(x)))
        t=" ".join(sentences[:2])
        if 40<len(t):
            found.append((t[:550].rsplit(" ",1)[0]+"...") if len(t)>550 else t)
    return found[:2]
def approach(q):
    low=q.lower()
    if any(x in low for x in ("attack","injection","malicious","security","permission","poison")):
        return "Apply an explicit trust boundary, least-privilege allowlist and test rejection of unauthorized calls with auditable traces."
    if any(x in low for x in ("benchmark","evaluate","latency","accuracy","cost","measure","metric","ablati","trade-off")):
        return "Specify ground-truth tasks, baseline, a held-out evaluation split and separate reliability, cost and latency metrics; do not mistake deterministic proxies for LLM evidence."
    if any(x in low for x in ("context","memory","retriev","cache","budget","progressive")):
        return "Separate metadata discovery from body loading, measure accessible context and prevent cross-agent state leakage."
    if any(x in low for x in ("subagent","orchestrat","playbook","delegat","workflow")):
        return "Implement bounded delegation states, explicit agent permissions, failure routing and trace capture; compare against a simpler baseline."
    return "Define the concept, design a reproducible example, test positive and negative cases and explain architectural limitations."
def chapter(i,title):
    n=f"{i:02d}"
    body=(BOOK/f"manuscript/revised/{n}/chapter.md").read_text()
    ex=[];review=[];paragraphs=[]
    for heading,part in sections(body):
        low=heading.lower()
        if "exercise" in low and "lab extension" not in low and "specification" not in low:ex+=items(part)
        elif "review question" in low:review+=items(part)
        elif "references" not in low:
            paragraphs.extend(cleaned(p) for p in re.split(r"\n\s*\n",part) if 80<len(cleaned(p))<1700 and not cleaned(p).startswith(chr(96)*3))
    if not ex:ex=[f"Design and test a minimal architecture related to {title}, with explicit failure cases."]
    ex=list(dict.fromkeys(ex));review=list(dict.fromkeys(review))
    folder=ROOT/f"chapters/{n}";folder.mkdir(parents=True,exist_ok=True)
    labs=[f"[Lab {lab}](../../labs/{lab}/README.md)" for lab in LAB_MAP[n]]
    page=[f"# Chapter {n}: {title}","","## Practical exercises"]
    for j,q in enumerate(ex,1):page.extend(["",f"### E{j:02d}","",q])
    page.extend(["","## Review questions"])
    for j,q in enumerate(review,1):page.extend(["",f"### Q{j:02d}","",q])
    page.extend(["","## Reference implementations"]+["- "+s for s in labs]+[""])
    (folder/"exercises.md").write_text("\n".join(page))
    notes=[f"# Chapter {n}: Worked Answers","",
       "These notes provide chapter-based model-answer guidance. Open-ended design questions can admit more than one valid solution.","",
       "## Practical exercise solutions"]
    for j,q in enumerate(ex,1):
        ev=evidence(q,paragraphs)
        notes.extend(["",f"### E{j:02d}",q,"",
            "**Implementation:** "+approach(q),"",
            "**Verification:** validate normal use, ambiguous inputs, failure recovery, permissions and trace quality.",""])
        if ev:notes.extend(["**Reasoning from the textbook:** "+" ".join(ev),""])
        notes.extend(["**Reference code:** "+", ".join(labs)+".",""])
    notes.extend(["","## Review-question answers"])
    for j,q in enumerate(review,1):
        ev=evidence(q,paragraphs)
        notes.extend(["",f"### Q{j:02d}",q,"",
          "**Answer:** "+(" ".join(ev) if ev else approach(q)),"",
          "**Assessment criteria:** clarity, correctness, a concrete example, trade-offs and limitations.",""])
    notes.extend(["","## Scientific limitations","",
       "The linked Python fixtures validate deterministic behaviour, not comparative performance claims about LLMs."])
    (folder/"answers.md").write_text("\n".join(notes))
    short=f"https://github.com/danraid/The-Skill-Bottleneck-Exercises/tree/main/chapters/{n}"
    (folder/"README.md").write_text("\n".join([
       f"# Chapter {n}: {title}","",f"Canonical book URL: {short}","",
       "- [Exercises](exercises.md)","- [Worked answers](answers.md)",
       *["- "+x for x in labs],"",
       f"Book source: https://github.com/danraid/The-Skill-Bottleneck/blob/main/manuscript/revised/{n}/chapter.md",""]))
    return {"chapter":n,"title":title,"exercises":len(ex),"questions":len(review),"labs":LAB_MAP[n]}
def main():
    cfg=json.loads((BOOK/"config/book.json").read_text())
    specs=json.loads((BOOK/"labs/specifications.json").read_text())["specs"]
    chapters=[chapter(i,rec[0]) for i,rec in enumerate(cfg["chapters"],1)]
    assert len(chapters)==20
    for spec in specs:
        n=spec["number"];src=BOOK/f"labs/generated/{n}"
        if not src.is_dir():raise RuntimeError("Canonical lab missing: "+n)
        out=ROOT/f"labs/{n}";out.mkdir(parents=True,exist_ok=True)
        for item in ("main.py","test_lab.py","execution.json","generation.json"):
            shutil.copy2(src/item,out/item)
        if json.loads((out/"execution.json").read_text()).get("exit_code")!=0:
            raise RuntimeError("Canonical lab did not pass: "+n)
        (out/"README.md").write_text("\n".join([
           f"# Laboratory {n}: {spec['title']}","",
           f"**Learning objective:** {spec['objective']}","",
           f"**Interface contract:** {spec['interface_contract']}","",
           f"**Acceptance criteria:** {spec['acceptance_criteria']}","",
           "## Running the reference solution","","Python 3.12, standard library only:","",
           "    python -m unittest -v test_lab.py","",
           "- [Reference implementation](main.py)",
           "- [Tests and executable assessment cases](test_lab.py)",
           "- [Original test evidence](execution.json)","",
           "This laboratory is an offline teaching prototype, not an empirical LLM benchmark.",""]))
    lines=["# The Skill Bottleneck: Exercises and Answers","",
       "Daniel Raaid | Official textbook companion exercises, model-answer notes and Python laboratories.","",
       "## Chapters","",
       "| Chapter | Exercises | Answers | Laboratories |",
       "|:--|:--|:--|:--|"]
    for c in chapters:
        n=c["chapter"];labs=", ".join(f"[{s}](labs/{s}/README.md)" for s in c["labs"])
        lines.append(f"| {n}: {c['title']} | [Exercises](chapters/{n}/exercises.md) | [Answers](chapters/{n}/answers.md) | {labs} |")
    lines.extend(["","## Usage","",
       "- [Installation and test instructions](RUNNING.md)",
       "- [Evidence and editorial limitations](EDITORIAL_NOTES.md)",
       "- [The book](https://github.com/danraid/The-Skill-Bottleneck)",""])
    (ROOT/"README.md").write_text("\n".join(lines))
    (ROOT/"RUNNING.md").write_text("# Running the exercises\n\nPython 3.12, standard library only.\n\nInside each lab directory execute:\n\n    python -m unittest -v test_lab.py\n")
    (ROOT/"EDITORIAL_NOTES.md").write_text(
       "# Provenance and limitations\n\nMaterials are derived from the source book, "
       "with answer guidance grounded in chapter passages. Code and tests were copied "
       "from the canonical 14-lab book pipeline with source-bound observed execution records. "
       "Some open-ended exercises do not have unique correct solutions. "
       "Passing synthetic fixture tests does not show actual multi-model performance.\n")
    report={"chapters":chapters,"labs":len(specs),"exercises":sum(c["exercises"] for c in chapters),
        "review_questions":sum(c["questions"] for c in chapters)}
    (ROOT/"content-manifest.json").write_text(json.dumps(report,indent=2)+"\n")
    print("BUILD_COMPLETED",json.dumps({"chapters":len(chapters),"labs":len(specs),
      "exercises":report["exercises"],"review_questions":report["review_questions"]}),flush=True)
if __name__=="__main__":
    main()
