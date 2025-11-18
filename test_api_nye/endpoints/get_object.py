import allure

import requests

from test_api_nye.endpoints.endpoint import Endpoint


class GetObject(Endpoint):
    @allure.step('Send a request to get all object')
    def get_all_objects(self, headers=None):
        headers = headers or self.headers
        self.response = requests.get(
            self.BASE_URL,
            headers=headers
        )

        self.response_json = self.response.json()
        return self.response

    @allure.step('Send a request to get a specific object')
    def get_specific_object(self, object_id):
        self.response = requests.get(
            f'{self.BASE_URL}/{object_id}',
            headers=self.headers
        )

        self.response_json = self.response.json()
        return self.response
