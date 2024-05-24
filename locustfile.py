from locust import HttpUser, task, between
from random import randint
class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Users will wait between 1 and 5 seconds between tasks

    def on_start(self):
        # This method will run when a user starts the test
        self.client.post("/add_user", json={"user_id": "123", "name": "name"})
        
        pass

    @task
    def load_test(self):
        self.client.get("/get_user?user_id=123")  # Replace with the endpoint you want to test

    @task
    def load_test(self):
        id = randint(1, 65535)
        self.client.post("/add_user", json={f"user_id": {id}, "name": "John Doe{id}"})
    
    @task
    def load_test(self):
        self.client.delete("/delete_user?user_id=123")

# Run the test
