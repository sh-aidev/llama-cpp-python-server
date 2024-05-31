from llama_cpp import Llama, LlamaGrammar
from llama_cpp.llama_chat_format import Llava15ChatHandler
from typing import List, Dict, Any
from src.utils.logger import logger
from src.utils.configs import LLMConfig
from src.utils.s3 import download_from_s3
from src.utils.openai_protocol import ChatCompletionResponse

class LlamaCppMultimodal():
    def __init__(
            self,
            cfg: LLMConfig,
            ) -> None:
        logger.debug(f"Initializing LlamaCpp Multimodal...")
        model_path, clip_model_path = download_from_s3(cfg)
        logger.debug(f"model path: {model_path}, n_ctx: {cfg.llm_config.llm.n_ctx}, n_threads: {cfg.llm_config.llm.n_threads}")
        chat_handler = Llava15ChatHandler(clip_model_path=clip_model_path)
        logger.debug(f"Initialized Chat Handler for Llava15")
        self.llm = Llama(model_path = model_path, chat_handler = chat_handler, n_ctx = cfg.llm_config.llm.n_ctx, n_threads = cfg.llm_config.llm.n_threads)
        logger.debug(f"Initialized LlamaCpp Multimodal")


    def predict(self, messages:List[Dict[str, Any]], grammar_txt: str, max_tokens: int = 32) -> str:

        if grammar_txt:
            grammar_txt = LlamaGrammar.from_string(grammar_txt)

        response =  self.llm.create_chat_completion(messages = messages, grammar=grammar_txt, max_tokens=max_tokens)

        logger.debug(f"Response: {response}")

        return ChatCompletionResponse(**response)
