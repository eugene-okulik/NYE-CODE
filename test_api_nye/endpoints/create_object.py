import allure

import requests

from test_api_nye.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    @allure.step('Send a create post request')
    def create_object(self, payload, headers=None):
        headers = headers or self.headers
        self.response = requests.post(
            self.BASE_URL,
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json()
        return self.response
