from fastapi.testclient import TestClient
from new_proj.main import app
from new_proj.settings import settings


def test_status_answer():
    client = TestClient(app)
    result = client.get(settings.main_url)
    assert result.status_code == 200
    assert result.json() == {"status": "OK"}
