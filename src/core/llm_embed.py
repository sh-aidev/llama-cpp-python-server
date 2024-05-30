from sentence_transformers import SentenceTransformer

from src.utils.logger import logger
from src.utils.configs import LLMConfig

class LLMEmbed():
    def __init__(
            self,
            cfg: LLMConfig,
            ) -> None:
        logger.debug(f"Initializing LlamaCpp")

        self.embed = SentenceTransformer(cfg.llm_config.embed.name)

    def encode(self, text:str) -> str:

        return self.embed.encode(text, normalize_embeddings=True)