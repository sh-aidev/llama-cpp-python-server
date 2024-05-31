import os
import openai
from openai import OpenAI
from typing import List, Dict
from src.utils.logger import logger
from src.utils.configs import LLMConfig


class LLMOpenAI():
    def __init__(self, cfg: LLMConfig):
        logger.debug(f"Initializing Gpt4")
        self.cfg = cfg

        openai.api_key = os.getenv("OPENAI_KEY")

    def predict(self, model_name:str, messages: List[Dict[str,str]], max_tokens: int = 32) -> str:
        response = openai.chat.completions.create(
            model=model_name if model_name is not None else self.cfg.llm_config.llm.name,
            messages=messages,
            max_tokens=max_tokens
        )
        logger.debug(f"GPT4 Response: {response}")
        # return response.choices[0].message.content
        return response

class EmbedOpenAI():
    def __init__(self):
        logger.debug(f"Initializing Embed OpenAI")

        self.client = OpenAI(
            api_key=os.getenv("OPENAI_KEY")
        )

    def encode(self, text: str, model:str) -> list:
        response = self.client.embeddings.create(
            input=[text],
            model=model,
        )
        return response