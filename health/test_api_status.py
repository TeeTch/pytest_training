import pytest


@pytest.mark.health
def test_health(health):
    assert health.status_code == 200
