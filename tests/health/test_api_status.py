import pytest
import requests

from tests.support.requests.api_requests import users


@pytest.mark.health
def test_health():
    # GIVEN
    response = requests.get(url=users['url'])
    # THEN
    assert response.status_code == 200
