"""Illustrative safer counterparts; validate in the full application context."""
import hashlib, hmac, subprocess
from pathlib import Path
from urllib.parse import urlparse

def get_user_record_safely(db, user_id):
    return db.execute("SELECT * FROM users WHERE id = ?", (user_id,))

def run_converter_safely(validated_filename):
    return subprocess.run(["convert", validated_filename, "/tmp/output.pdf"],
                          shell=False, check=True, timeout=10)

def read_file_safely(root, requested_name):
    root_path = Path(root).resolve()
    target = (root_path / requested_name).resolve()
    if target != root_path and root_path not in target.parents:
        raise ValueError("Path escapes allowed directory")
    return target.read_text(encoding="utf-8")

def password_hmac(value: bytes, supplied: str, secret: bytes):
    expected = hmac.new(secret, value, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, supplied)

def validate_url(url):
    # Illustrative only: production SSRF defense also needs DNS/IP and redirect controls.
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.hostname:
        raise ValueError("HTTPS URL required")
    return parsed
