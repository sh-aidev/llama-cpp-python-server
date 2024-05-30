from llama_cpp import Llama, LlamaGrammar
import os
import json
from src.utils.logger import logger
from src.utils.configs import LLMConfig
from src.utils.s3 import download_from_s3

class LlamaCpp():
    def __init__(
            self,
            cfg: LLMConfig,
            ) -> None:
        logger.debug(f"Initializing LlamaCpp")
        model_path = download_from_s3(model_name = cfg.llm_config.llm.name, bucket_name = cfg.llm_config.s3.bucket, src_file_path = cfg.llm_config.s3.root_path)

        logger.debug(f"model path: {model_path}, n_ctx: {cfg.llm_config.llm.n_ctx}, n_threads: {cfg.llm_config.llm.n_threads}")

        self.llm = Llama(model_path = model_path, n_ctx = cfg.llm_config.llm.n_ctx, n_threads = cfg.llm_config.llm.n_threads)

    def predict(self, text:str, grammar_txt: str, max_tokens: int = 32) -> str:
        
        if grammar_txt:
            grammar_txt = LlamaGrammar.from_string(grammar_txt)

        return self.llm(text, grammar=grammar_txt, max_tokens=max_tokens)['choices'][0]['text']
        