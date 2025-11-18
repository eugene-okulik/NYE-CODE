import pytest

TEST_DATA_1 = [
    {"name": "TestObject1", "data": {"color": "red", "size": "medium"}},
    {"name": "TestObject2", "data": {"color": "blue", "size": "small"}},
    {"name": "TestObject3", "data": {"color": "green", "size": "big"}}
]

TEST_DATA_2 = [
    {"name": "MyObjectUpdated", "data": {"color": "green", "size": "large"}}
]


def test_get_all_objects_test(get_object_endpoint):
    get_object_endpoint.get_all_objects()
    get_object_endpoint.check_response_status_code(200)
    get_object_endpoint.check_response_contains_objects()


def test_get_object_endpoint(get_object_endpoint, create_new_object):
    get_object_endpoint.get_specific_object(create_new_object)
    get_object_endpoint.check_response_status_code(200)
    get_object_endpoint.check_response_contains_objects()


@pytest.mark.parametrize('data', TEST_DATA_1)
def test_create_object(create_object_endpoint, data):
    create_object_endpoint.create_object(payload=data)
    create_object_endpoint.check_response_status_code(200)
    create_object_endpoint.check_response_name(data["name"])


@pytest.mark.parametrize('data', TEST_DATA_2)
def test_update_object_test(update_object_endpoint, create_new_object, data):
    update_object_endpoint.update_object(object_id=create_new_object, payload=data)
    update_object_endpoint.check_response_status_code(200)
    update_object_endpoint.check_response_name(data["name"])


def test_delete_object_test(delete_object_endpoint, create_new_object):
    delete_object_endpoint.delete_object(create_new_object)
    delete_object_endpoint.check_response_status_code(200)
