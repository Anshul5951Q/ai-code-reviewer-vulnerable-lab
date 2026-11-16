# AI Code Reviewer Vulnerability Lab

Deliberately vulnerable **static-analysis fixtures only**. Do not deploy, expose publicly, or run vulnerable functions with untrusted input. Use a private/disposable GitHub repository.

Contents:
- `python_app/vulnerable.py`: SQL injection, command injection, unsafe pickle, path traversal, SSRF, MD5 password digest, reflected HTML.
- `javascript_app/vulnerable.js`: command injection, DOM XSS, eval/code injection, path traversal.
- `safe_examples/`: illustrative safer counterparts.
- `fixtures/`: fake test secret, insecure Dockerfile, old dependency pins.
- `EXPECTED_FINDINGS.md`: seeded issues and CWE mapping.
- `TESTING_GUIDE.md`: testing instructions.

Push the extracted folder contents to a private GitHub repository, connect it to your reviewer, select the default branch and latest commit, then run analysis. Compare actual findings and evidence with the expected inventory. Scanner coverage varies; do not expect identical counts.

Never add real credentials or deploy this project.
