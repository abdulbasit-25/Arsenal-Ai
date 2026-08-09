import os
from pathlib import Path


def _get_env(name: str) -> str:
    value = os.getenv(name, "")
    return (value or "").strip()


def get_gemini_api_key() -> str:
    return _get_env("GEMINI_API_KEY")


def get_openrouter_api_key() -> str:
    return _get_env("OPENROUTER_API_KEY")


def get_gemini_live_model() -> str:
    return _get_env("GEMINI_LIVE_MODEL") or "gemini-2.0-flash-live-001"


def get_config_summary() -> dict:
    return {
        "gemini_configured": bool(get_gemini_api_key()),
        "openrouter_configured": bool(get_openrouter_api_key()),
        "gemini_live_model": get_gemini_live_model(),
    }
