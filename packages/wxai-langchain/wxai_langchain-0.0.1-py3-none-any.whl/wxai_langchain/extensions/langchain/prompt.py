import requests

class Prompt:
    def __init__(self, access_token, project_id, api_endpoint):
        self.access_token = access_token
        self.project_id = project_id
        self.api_endpoint = api_endpoint

    def generate(self, input, model_id, parameters):
        wml_url = self.api_endpoint
        Headers = {
            "Authorization": "Bearer " + self.access_token,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        data = {
            "model_id": model_id,
            "input": input,
            "parameters": parameters,
            "project_id": self.project_id
        }
        response = requests.post(wml_url, json=data, headers=Headers)
        if response.status_code == 200:
            return response.json()["results"][0]["generated_text"]
        else:
            return response.text