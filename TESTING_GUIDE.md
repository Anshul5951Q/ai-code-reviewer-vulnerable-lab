# Testing safely

1. Create a private or disposable GitHub repository.
2. Extract this ZIP and push the folder contents to its root.
3. Connect it to AI Code Reviewer and analyze the latest commit.
4. Verify discovered/downloaded/parsed/analyzed file counts.
5. Inspect each finding's path, line range, evidence, CWE, severity and scanner provenance.
6. Confirm the safe examples are not flagged for the corresponding unsafe pattern.
7. Record unsupported categories and unavailable scanners as coverage gaps.

Do not execute the vulnerable functions or deploy this project. It is designed for static analysis. A zero-finding result is not proof of safety. Do not expect every scanner to detect every seeded category.
