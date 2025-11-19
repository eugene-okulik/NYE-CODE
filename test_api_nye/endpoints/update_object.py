import allure

import requests

from test_api_nye.endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):
    @allure.step('Send an update object put request')
    def update_object(self, object_id, payload, headers=None):
        headers = headers or self.headers
        self.response = requests.put(
            f'{self.BASE_URL}/{object_id}',
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json()
        return self.response
