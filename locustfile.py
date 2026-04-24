from locust import HttpUser, task, between
import os


class PetStoreUser(HttpUser):
    host = os.getenv("LOCUST_HOST")
    wait_time = between(1, 3)

    @task(3)
    def get_pets_by_status(self):
        self.client.get("/v2/pet/findByStatus?status=available")

    @task(2)
    def get_pet_by_id(self):
        with self.client.get("/v2/pet/1", catch_response=True) as response:
            if response.status_code == 404:
                response.success()

    @task(1)
    def get_store_inventory(self):
        self.client.get("/v2/store/inventory")