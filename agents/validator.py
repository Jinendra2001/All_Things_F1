from llm.llm import LLM

class Validator:
    
    prompt = "The first query is the user input and the second query is the summary of the driver performance. Validate the user query with the summary and give a final VERDICT THE THE SUMMARY IS TRUE OR FALSE. And the response should be in a clean text paragraph format without any list or bullet points"
    
    def validator(self, query, summary):
        llm = LLM()
        contents = f"User Query: {query}\nSummary: {summary}"
        response = llm.generate_content(contents)
        return response