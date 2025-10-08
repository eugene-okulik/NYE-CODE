import requests

BASE_URL = "http://objapi.course.qa-practice.com"


def get_all_objects():
    response = requests.get(f"{BASE_URL}/object").json()
    return response


def create_new_object():
    body = {
        "name": "TestObject",
        "data": {"color": "red", "size": "small"}
    }
    response = requests.post(f"{BASE_URL}/object", json=body)
    assert response.status_code == 200, "Не удалось создать объект"
    return response.json()["id"]


def get_object_by_id():
    object_id = create_new_object()
    response = requests.get(f"{BASE_URL}/object/{object_id}").json()
    assert response["id"] == object_id
    return response


def create_object_test():
    body = {
        "name": "MyObject",
        "data": {"color": "blue", "size": "medium"}
    }
    response = requests.post(f"{BASE_URL}/object", json=body)
    assert response.status_code == 200, "Не удалось создать объект"
    assert response.json()["name"] == "MyObject"
    return response.json()["id"]


def update_object_test():
    object_id = create_new_object()
    body = {
        "name": "MyObjectUpdated",
        "data": {"color": "green", "size": "large"}
    }
    response = requests.put(f"{BASE_URL}/object/{object_id}", json=body).json()
    assert response["name"] == "MyObjectUpdated"
    clear_object(object_id)
    return object_id


def patch_object_test():
    object_id = create_new_object()
    body = {"data": {"color": "yellow"}}
    response = requests.patch(f"{BASE_URL}/object/{object_id}", json=body).json()
    assert response["data"]["color"] == "yellow"
    clear_object(object_id)
    return object_id


def delete_object_test():
    object_id = create_new_object()
    response = requests.delete(f"{BASE_URL}/object/{object_id}")
    assert response.status_code == 200


def clear_object(object_id):
    requests.delete(f"{BASE_URL}/object/{object_id}")


print(get_all_objects())
print(get_object_by_id())
update_object_test()
patch_object_test()
delete_object_test()
