import allure

import requests

from test_api_nye.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):
    @allure.step('Send a delete object request')
    def delete_object(self, object_id, headers=None):
        headers = headers or self.headers
        self.response = requests.delete(
            f'{self.BASE_URL}/{object_id}',
            headers=headers
        )
        self.response_text = self.response.text
        return self.response
