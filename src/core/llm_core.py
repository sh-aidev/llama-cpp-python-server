from llama_cpp import Llama, LlamaGrammar
from typing import List, Dict, Any

from src.utils.logger import logger
from src.utils.configs import LLMConfig
from src.utils.s3 import download_from_s3
from src.utils.openai_protocol import ChatCompletionResponse

class LlamaCpp():
    def __init__(
            self,
            cfg: LLMConfig,
            ) -> None:
        logger.debug(f"Initializing LlamaCpp")
        model_path = download_from_s3(cfg)

        logger.debug(f"model path: {model_path}, n_ctx: {cfg.llm_config.llm.n_ctx}, n_threads: {cfg.llm_config.llm.n_threads}")

        self.llm = Llama(model_path = model_path, n_ctx = cfg.llm_config.llm.n_ctx, n_threads = cfg.llm_config.llm.n_threads)

    def predict(self, messages:List[Dict[str, Any]], grammar_txt: str, max_tokens: int = 32) -> str:
        
        if grammar_txt:
            grammar_txt = LlamaGrammar.from_string(grammar_txt)

        response =  self.llm.create_chat_completion(messages = messages, grammar=grammar_txt, max_tokens=max_tokens)

        logger.debug(f"Response: {response}")

        return ChatCompletionResponse(**response)
        