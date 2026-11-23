# Running The Skill Bottleneck Laboratories

Use **Python 3.12**. The 14 lab prototypes use only the Python standard library.

From the repository root:

    cd labs/01
    python -m unittest -v test_lab.py

Repeat for lab directories 01 through 14. The continuous-integration workflow runs every test suite and checks that all 20 chapter exercise and solution targets exist.

The JSON execution record in each lab is original source-bound evidence from the book-production workflow. Re-running the tests locally is recommended. Neither the recorded results nor passing unit tests establish comparative performance for real LLM models.
