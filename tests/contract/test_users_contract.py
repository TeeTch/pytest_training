import pytest
import requests

from tests.support.assertions import assert_valid_schema
from tests.support.requests.api_requests import users
from tests.support.requests.test_values import valid_test_data_post


@pytest.mark.contract
def test_get_users_200():
    # GIVEN
    response = requests.get(url=users['url'])
    json_data = response.json()
    # THEN
    assert response.status_code == 200
    assert_valid_schema(json_data, 'users.json')


@pytest.mark.contract
def test_get_user_200():
    # GIVEN
    response = requests.get(url=users['url'] + '/2')
    json_data = response.json()
    # THEN
    assert response.status_code == 200
    assert_valid_schema(json_data, 'user.json')


@pytest.mark.contract
def test_get_user_404():
    # GIVEN
    response = requests.get(url=users['url'] + '/23')
    # json_data = response.json()
    # THEN
    assert response.status_code == 404


@pytest.mark.contract
def test_post_single_user_201():
    # GIVEN
    payload = valid_test_data_post
    response = requests.post(url=users['url'], data=payload)
    json_data = response.json()
    # THEN
    assert response.status_code == 201
    assert_valid_schema(json_data, 'new_user.json')


@pytest.mark.contract
def test_update_user_200():
    # GIVEN
    payload = valid_test_data_post
    response = requests.put(url=users['url'] + '/2', data=payload)
    json_data = response.json()
    # THEN
    assert response.status_code == 200
    assert_valid_schema(json_data, 'update_user.json')


@pytest.mark.contract
def test_delete_user_204():
    # GIVEN
    response = requests.delete(url=users['url'] + '/2')
    # THEN
    assert response.status_code == 204
