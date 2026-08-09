import asyncio
import types
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from main import JarvisLive


class DummyUI:
    def __init__(self):
        self.muted = False

    def set_state(self, state):
        self.state = state

    def write_log(self, *args, **kwargs):
        pass

    def wait_for_api_key(self):
        pass


class DummySession:
    def __init__(self, exc):
        self.exc = exc

    async def __aenter__(self):
        raise self.exc

    async def __aexit__(self, exc_type, exc, tb):
        return False


class DummyClient:
    def __init__(self, exc):
        self.exc = exc

    @property
    def aio(self):
        return self

    @property
    def live(self):
        return self

    def connect(self, *args, **kwargs):
        return DummySession(self.exc)


def test_run_stops_after_connection_error(monkeypatch):
    async def fake_sleep(_):
        raise asyncio.CancelledError

    ui = DummyUI()
    jarvis = JarvisLive(ui)
    jarvis._build_config = lambda: {}

    async def fake_run(self):
        raise RuntimeError('boom')

    monkeypatch.setattr('main.asyncio.sleep', fake_sleep)
    monkeypatch.setattr('main.genai.Client', lambda *args, **kwargs: DummyClient(RuntimeError('boom')))

    async def runner():
        try:
            await jarvis.run()
        except asyncio.CancelledError:
            pass

    asyncio.run(runner())
