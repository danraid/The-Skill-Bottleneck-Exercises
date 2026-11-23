"""Deterministic lexical skill router, educational prototype.

The task domain is represented by the leading query term for this *fixture*.
A candidate is eligible when that domain term occurs anywhere in its tokens.
This avoids the invalid assumption that skill descriptions always start with
their domain (for example, "Senior Python developer").

This is lexical token overlap, not an embedding-based semantic similarity model.
"""
from __future__ import annotations

import re
from typing import List


def _tokenize(text: str) -> set[str]:
    return {term for term in re.split(r"\W+", text.casefold()) if term}


def _jaccard(first: set[str], second: set[str]) -> float:
    if not first and not second:
        return 1.0
    if not first or not second:
        return 0.0
    return len(first & second) / len(first | second)


def route(query: str, skills: List[str], k: int) -> List[str]:
    """Rank domain-compatible descriptions by lexical Jaccard similarity.

    Query's first token is a fixture-level domain label, not a production
    intent classifier. For production, pass an explicit structured domain
    argument and use a calibrated semantic retrieval model.
    """
    if not isinstance(query, str):
        raise TypeError("query must be a string")
    if not isinstance(skills, list) or any(not isinstance(s, str) for s in skills):
        raise TypeError("skills must be a list of strings")
    if not isinstance(k, int) or isinstance(k, bool):
        raise TypeError("k must be an integer")
    if k <= 0:
        return []
    query_tokens = _tokenize(query)
    if not query_tokens:
        return [s for s in skills if not _tokenize(s)][:k]
    query_domain = re.split(r"\W+", query.strip().casefold())[0]
    ranked = []
    for index, skill in enumerate(skills):
        skill_tokens = _tokenize(skill)
        if query_domain not in skill_tokens:
            continue
        ranked.append((_jaccard(query_tokens, skill_tokens), index, skill))
    ranked.sort(key=lambda x: (-x[0], x[1]))
    return [skill for _, _, skill in ranked[:k]]

