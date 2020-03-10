import pytest

from support.assertions import assert_valid_schema


@pytest.mark.contract
def test_get_users_200(health):
    json_data = health.json()

    assert health.status_code == 200
    assert_valid_schema(json_data, 'users.json')


@pytest.mark.contract
def test_get_user_200(get_user):
    json_data = get_user.json()

    assert get_user.status_code == 200
    assert_valid_schema(json_data, 'user.json')


@pytest.mark.contract
def test_get_user_404(get_user_404):
    assert get_user_404.status_code == 404


@pytest.mark.contract
def test_post_single_user_201(post_new_user):
    json_data = post_new_user.json()

    assert post_new_user.status_code == 201
    assert_valid_schema(json_data, 'new_user.json')


@pytest.mark.contract
def test_update_user_200(post_new_user):
    json_data = post_new_user.json()

    assert post_new_user.status_code == 201
    assert_valid_schema(json_data, 'new_user.json')


@pytest.mark.contract
def test_delete_user_200(delete_user):
    assert delete_user.status_code == 204
