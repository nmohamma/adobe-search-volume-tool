"""
Secure config loader for Adobe Stock Search Volume app.
Loads secrets from .env file (never committed to git).
"""
import os
from pathlib import Path

# Project root
PROJECT_DIR = Path(__file__).parent.resolve()
ENV_FILE = PROJECT_DIR / ".env"

def load_env():
    """Load .env file if it exists."""
    if not ENV_FILE.exists():
        return {}
    env = {}
    with open(ENV_FILE) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip("'\"")
    return env

_env = load_env()

JINA_API_KEY = _env.get("JINA_API_KEY") or os.environ.get("JINA_API_KEY")
JINA_READER_URL = "https://r.jina.ai"
