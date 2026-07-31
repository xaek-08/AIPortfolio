import ollama
from typing import List

class Generator:
    def __init__(self,model:str="qwen2:7b"):
        self.model=model

    def build_prompt(self,query:str,contexts:List[str])->str:
        context="\n\n".join(contexts)
        prompt=f"""
            You are a helpful assistant.
            Answer only using the provided context.
            Also mention which diary entry you used (for example, the date or other metadata).
            If the answer cannot be found,say:
            "I don't know based on the provided context."
            Context:
            {context}
            Question:
            {query}
            Answer:
        """
        return prompt

    def generate(self,query:str,contexts:List[str])->str:
        prompt=self.build_prompt(query,contexts)
        response=ollama.chat(
            model=self.model,
            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )
        return response["message"]["content"]