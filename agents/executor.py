import time
import requests
from llm.llm import LLM


class Executor:
     
    
    def fetch_data_from_api(self,urls,max_retries=5):
        delay = 1
        for url in urls:
            for attempt in range(max_retries):
                try:
                    response = requests.get(url)
                    response.raise_for_status()
                    yield response.json()
                    break 
                except requests.RequestException as error:
                    if attempt == max_retries - 1:
                        print(f"Error fetching data: {error}")
                        # skip this url after exhausting retries
                        break
                    sleep_time = delay * (2 ** attempt)
                    print(f"Request failed (attempt {attempt + 1}/{max_retries}). Retrying in {sleep_time} seconds...")
                    time.sleep(sleep_time)
                    
    
    prompt = "Analyse the data and query and then give a Short summary accordingly. And the response should be in a clean text paragraph format without any list or bullet points"
    
    def executor(self, query, urls):
        data = list(self.fetch_data_from_api(urls))
        llm = LLM()
        contents = f"Data: {data}\nQuery: {query}"
        response = llm.generate_content(contents)
        summary = response
        return summary  