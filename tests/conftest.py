import pytest
import requests

from support.requests.api_requests import *
from support.requests.test_values import *


@pytest.fixture
def health():
    response = requests.get(url=users['url'])

    return response


@pytest.fixture
def get_user():
    single_user = users['url'] + '/2'
    response = requests.get(url=single_user)

    return response


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
    response = requests.put(url=single_user, data=payload)

    return response


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
