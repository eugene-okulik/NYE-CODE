import allure


class Endpoint:
    BASE_URL = "http://objapi.course.qa-practice.com/object"
    response = None
    response_json = None
    response_text = None
    headers = {"Content-Type": "application/json"}

    @allure.step("Check the response name")
    def check_response_name(self, expected_name):
        assert self.response_json["name"] == expected_name

    @allure.step('Check the response status code')
    def check_response_status_code(self, status_code):
        assert self.response.status_code == status_code, "Не удалось создать объект"

    @allure.step('Check the response contains object')
    def check_response_contains_objects(self):
        assert len(self.response_json) > 0, "Объекты не найдены"
