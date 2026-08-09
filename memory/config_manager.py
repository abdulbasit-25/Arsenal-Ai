import os
import sys
from pathlib import Path


def get_base_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).resolve().parent.parent


BASE_DIR = get_base_dir()
CONFIG_DIR = BASE_DIR / "config"


def ensure_config_dir() -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)


def save_api_keys(gemini_api_key: str) -> None:
    ensure_config_dir()
    os.environ["GEMINI_API_KEY"] = gemini_api_key.strip()


def load_api_keys() -> dict:
    return {
        "gemini_api_key": os.getenv("GEMINI_API_KEY", "").strip(),
        "openrouter_api_key": os.getenv("OPENROUTER_API_KEY", "").strip(),
    }


def get_gemini_key() -> str | None:
    return load_api_keys().get("gemini_api_key")


def is_configured() -> bool:
    key = get_gemini_key()
    return bool(key and len(key) > 15)