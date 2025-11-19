import pytest

from test_api_nye.endpoints.create_object import CreateObject
from test_api_nye.endpoints.delete_object import DeleteObject
from test_api_nye.endpoints.get_object import GetObject
from test_api_nye.endpoints.update_object import UpdateObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def create_new_object(create_object_endpoint, delete_object_endpoint):
    payload = {"name": "TempObject", "data": {"color": "white", "size": "small"}}
    create_object_endpoint.create_object(payload)
    create_object_endpoint.check_response_status_code(200)
    object_id = create_object_endpoint.response_json["id"]
    print("object_id: ", object_id)
    yield object_id
    delete_object_endpoint.delete_object(object_id)
