import pytest
import requests

from tests.support.assertions import assert_valid_schema
from tests.support.requests.api_requests import registration


@pytest.mark.parametrize("payload, response_status, schema", [({"email": "eve.holt@reqres.in", "password": "cityslicka"}, 200, 'registration.json'), ({"email": "eve.holt@reqres.in"}, 400, 'error.json')], ids=["200", "400"])
@pytest.mark.contract
def test_registration_contract(payload, response_status, schema):
    # GIVEN
    data = payload
    response = requests.post(url=registration['url'], data=data)
    json_data = response.json()
    # THEN
    assert response.status_code == response_status
    assert_valid_schema(json_data, schema)
