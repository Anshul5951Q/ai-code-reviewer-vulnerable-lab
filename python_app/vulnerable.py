"""INTENTIONALLY VULNERABLE STATIC-ANALYSIS FIXTURES. DO NOT DEPLOY OR RUN."""
import hashlib
import os
import pickle
import subprocess
from pathlib import Path
import requests

def get_user_record(db, user_id: str):
    # PY-01 SQL injection: untrusted input concatenated into SQL.
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    return db.execute(query)

def convert_document(user_filename: str):
    # PY-02 command injection: user input enters a shell command.
    command = f"convert {user_filename} /tmp/output.pdf"
    return subprocess.run(command, shell=True, check=False)

def load_session(serialized_session: bytes):
    # PY-03 unsafe deserialization of externally supplied bytes.
    return pickle.loads(serialized_session)

def read_profile_file(root: str, requested_name: str):
    # PY-04 path traversal: no canonical path containment validation.
    target = os.path.join(root, requested_name)
    return Path(target).read_text(encoding="utf-8")

def fetch_remote_preview(url: str):
    # PY-05 SSRF: caller-controlled URL fetched without destination validation.
    return requests.get(url, timeout=5)

def legacy_password_digest(password: str):
    # PY-06 MD5 is unsuitable for password storage.
    return hashlib.md5(password.encode("utf-8")).hexdigest()

def render_comment(comment: str):
    # PY-07 untrusted text embedded in an HTML response.
    return "<div class='comment'>" + comment + "</div>"
