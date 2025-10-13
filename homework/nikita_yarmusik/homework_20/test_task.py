import pytest

import requests


BASE_URL = "http://objapi.course.qa-practice.com"


@pytest.fixture()
def create_new_object():
    body = {
        "name": "TestObject",
        "data": {"color": "red", "size": "small"}
    }
    response = requests.post(f"{BASE_URL}/object", json=body)
    assert response.status_code == 200, "Не удалось создать объект"
    object_id = response.json()["id"]
    yield object_id
    requests.delete(f"{BASE_URL}/object/{object_id}")


@pytest.fixture(scope="session")
def run_test_notification():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture(scope="function")
def split_test_notification():
    print("Before test")
    yield
    print("After test")


@pytest.mark.medium
def test_get_all_objects(create_new_object, run_test_notification, split_test_notification):
    response = requests.get(f"{BASE_URL}/object")
    assert response.status_code == 200
    assert len(response.json()["data"]) > 1


@pytest.mark.critical
def test_get_object_by_id(create_new_object, split_test_notification):
    response = requests.get(f"{BASE_URL}/object/{create_new_object}")
    assert response.json()["id"] == create_new_object
    assert response.status_code == 200
    assert len(response.json()["data"]) > 0


@pytest.mark.parametrize('body', [
    {"name": "TestObject1", "data": {"color": "red", "size": "medium"}},
    {"name": "TestObject2", "data": {"color": "blue", "size": "small"}},
    {"name": "TestObject3", "data": {"color": "green", "size": "big"}}
])
def test_create_object_test(body, split_test_notification):
    response = requests.post(f"{BASE_URL}/object", json=body)
    assert response.status_code == 200, "Не удалось создать объект"
    assert response.json()["name"] == body["name"]


def test_update_object_test(create_new_object, split_test_notification):
    object_id = create_new_object
    body = {
        "name": "MyObjectUpdated",
        "data": {"color": "green", "size": "large"}
    }
    response = requests.put(f"{BASE_URL}/object/{object_id}", json=body).json()
    assert response["name"] == body["name"]


def test_patch_object_test(create_new_object, split_test_notification):
    object_id = create_new_object
    body = {"data": {"color": "yellow"}}
    response = requests.patch(f"{BASE_URL}/object/{object_id}", json=body).json()
    assert response["data"]["color"] == body["data"]["color"]


def test_delete_object_test(create_new_object, split_test_notification):
    object_id = create_new_object
    response = requests.delete(f"{BASE_URL}/object/{object_id}")
    assert response.status_code == 200
