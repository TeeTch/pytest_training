import pytest
import requests


@pytest.mark.health
def test_health(health):
    # GIVEN
    response = requests.get(url=health)
    # THEN
    assert response.status_code == 200
