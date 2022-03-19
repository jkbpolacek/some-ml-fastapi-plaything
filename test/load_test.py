from locust import HttpUser, TaskSet, task, between

class TitanicPredictSingle(TaskSet):
    @task
    def predict(self):
        request_body = [
            {
                "Pclass": 1,
                "Name": "Kelly",
                "Sex": "male",
                "Age": 34.5,
                "SibSp": 5,
                "Parch": 5,
                "Fare": 7.8292,
                "Embarked": "Q",
            }
        ]
        self.client.post("/predict", json=request_body)

class TitanicPredictMultiple(TaskSet):
    @task
    def predict_multiple(self):
        request_body = [
            {
                "Pclass": 1,
                "Name": "Kelly",
                "Sex": "male",
                "Age": 34.5,
                "SibSp": 5,
                "Parch": 5,
                "Fare": 7.8292,
                "Embarked": "Q",
            },
            {
                "Pclass": 2,
                "Name": "Kelly",
                "Sex": "male",
                "Age": 15.5,
                "SibSp": 5,
                "Parch": 5,
                "Fare": 7.8292,
                "Embarked": "Q",
            },
        ]
        self.client.post("/predict", json=request_body)


class LoadTest(HttpUser):
    tasks = [TitanicPredictSingle, TitanicPredictMultiple]
    host = "http://127.0.0.1"
    stop_timeout = 20
    wait_time = between(1, 5)
