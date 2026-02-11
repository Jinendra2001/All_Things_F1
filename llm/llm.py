import os
from dotenv import dotenv_values
from google import genai

class LLM:
    
    config = dotenv_values(".env")
    
    def __init__(self):
        self.client = genai.Client(api_key=self.config["GENAI_APIKEY"])
    
    def generate_content(self, contents):
        response = self.client.models.generate_content(model=self.config["GENAI_MODEL"], contents=contents)
        return response.text