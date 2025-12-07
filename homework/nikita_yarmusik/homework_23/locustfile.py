import random

from faker import Faker

from locust import HttpUser, between, task


class ObjectUser(HttpUser):
    host = "http://objapi.course.qa-practice.com"
    wait_time = between(1, 5)

    def on_start(self):
        self.faker = Faker()
        self.created_ids = []

    def generate_object_data(self):
        return {
            "name": f"{self.faker.unique.word()}_{self.faker.random_number(digits=3)}",
            "data": {
                "color": random.choice(["red", "black"]),
                "size": self.faker.random_element(["s", "m", "l", "xl", "xxl"])
            }
        }

    @task(2)
    def get_all_objects(self):
        self.client.get("/object", name="GET /object")

    @task(2)
    def create_object(self):
        payload = self.generate_object_data()
        response = self.client.post("/object", json=payload, name="POST /object")

        if response.status_code == 200:
            obj_id = response.json().get("id")
            if obj_id:
                self.created_ids.append(obj_id)

    @task(1)
    def get_object_by_id(self):
        if not self.created_ids:
            return

        obj_id = random.choice(self.created_ids)
        self.client.get(f"/object/{obj_id}", name="GET /object/{id}")
