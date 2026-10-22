from typing import Dict, Any
import requests

import prompts

class LLM:
    def __init__(self, model_name: str, ollama_url: str = 'http://localhost:11434'):
        self.ollama_url = ollama_url
        self.model_name = model_name

    def generate(self, prompt: str, temperature: float = 0.7, top_k: int = 40) -> Dict[str, Any]:
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
                "top_k": top_k
            }
        }

        response = requests.post(f"{self.ollama_url}/api/generate", json=payload)
        response.raise_for_status()
        data = response.json()

        generation_info = {
            'model_name': model_name,
            'prompt': prompt,
            'output_text': data['response'],
            'temperature': temperature,
            'top_k': top_k,
            'generatin_time_s': data['eval_duration'] / 1e9,
            'output_tokens_num': data['eval_count'],
            'tokens_per_sec': data['eval_count'] / data['eval_duration'] * 1e9
        }

        return generation_info

if __name__ == "__main__":
    import pandas as pd

    from prompts import prompts_list
    from llms import llms_list
    from auto_report import generate_report

    results = []

    for model_name in llms_list:
        model = LLM(model_name)
        for prompt in prompts_list:
            for temperature in [0.7, 0.2, 1]:
                for top_k in [40, 10, 100]:
                    results.append(model.generate(prompt=prompt, temperature=temperature, top_k=top_k))

    # result_df = pd.json_normalize(results)
    # result_df.to_csv("results/result.csv")
    # generate_report(
    #     lab_number=1,
    #     description="",
    #     results=str(result_df),
    #     conclusion=""
    # )

