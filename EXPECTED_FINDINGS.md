# Expected seeded findings

| ID | File | Issue | CWE |
|---|---|---|---|
| PY-01 | python_app/vulnerable.py | SQL injection | CWE-89 |
| PY-02 | python_app/vulnerable.py | Shell command injection | CWE-78 |
| PY-03 | python_app/vulnerable.py | Unsafe pickle deserialization | CWE-502 |
| PY-04 | python_app/vulnerable.py | Path traversal | CWE-22 |
| PY-05 | python_app/vulnerable.py | SSRF | CWE-918 |
| PY-06 | python_app/vulnerable.py | MD5 used for password digest | CWE-327 |
| PY-07 | python_app/vulnerable.py | Untrusted data embedded in HTML | CWE-79 |
| JS-01 | javascript_app/vulnerable.js | Shell command injection | CWE-78 |
| JS-02 | javascript_app/vulnerable.js | DOM XSS via innerHTML | CWE-79 |
| JS-03 | javascript_app/vulnerable.js | eval/code injection | CWE-94 |
| JS-04 | javascript_app/vulnerable.js | Path traversal | CWE-22 |
| CFG-01 | fixtures/example.env | Fake hardcoded test token | CWE-798 |
| CFG-02 | fixtures/Dockerfile.insecure | Container runs as root (no USER) | CWE-250 |
| DEP-01 | fixtures/requirements-vulnerable.txt | Old dependency versions; check current advisories | — |

Line numbers may change if files are edited. SSRF and authorization-like issues often need data-flow/framework context. This inventory is a test oracle, not a guarantee every scanner detects every item.
