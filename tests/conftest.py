import pytest
import requests

from tests.support.requests.api_requests import users
from tests.support.requests.test_values import valid_test_data_post, valid_test_data_put


@pytest.fixture
def health():
    url = users['url']

    return url


@pytest.fixture
def get_user():
    single_user = users['url'] + '/2'

    return single_user


@pytest.fixture
def get_user_404():
    single_user = users['url'] + '/23'
    response = requests.get(url=single_user)

    return response


@pytest.fixture
def post_new_user():
    payload = valid_test_data_post
    response = requests.post(url=users['url'], data=payload)

    return response


@pytest.fixture
def put_user():
    single_user = users['url'] + '/2'
    payload = valid_test_data_put

    return [single_user, payload]


@pytest.fixture
def patch_user():
    single_user = users['url'] + '/2'
    payload = valid_test_data_put['job']
    response = requests.patch(url=single_user, data=payload)

    return response


@pytest.fixture
def delete_user():
    single_user = users['url'] + '/23'
    response = requests.delete(url=single_user)

    return response
