import pytest
import requests

from tests.support.requests.api_requests import registration


@pytest.mark.parametrize("payload, response_status, response_keys", [({"email": "eve.holt@reqres.in", "password": "cityslicka"}, 200, ['token', 'id']), ({"email": "eve.holt@reqres.in"}, 400, ['error'])], ids=["valid email and password", "no password"])
@pytest.mark.contract
def test_registration(payload, response_status, response_keys):
    # GIVEN
    data = payload
    response = requests.post(url=registration['url'], data=data)
    json_data = response.json()
    # THEN
    assert response.status_code == response_status
    for response_key in response_keys:
        assert response_key in json_data
