from sentence_transformers import SentenceTransformer

from src.utils.logger import logger
from src.utils.configs import LLMConfig
from src.utils.openai_protocol import CreateEmbeddingResponse

class LLMEmbed():
    def __init__(
            self,
            cfg: LLMConfig,
            ) -> None:
        logger.debug(f"Initializing LlamaCpp Embeddings")
        self.cfg = cfg

        self.embed = SentenceTransformer(cfg.llm_config.embed.name)

    def encode(self, text:str) -> str:

        embedding_data =  self.embed.encode(text, normalize_embeddings=True)
        return CreateEmbeddingResponse(
            data=[
                {
                    "embedding": embedding_data,
                    "index": 0
                }
            ],
            model=self.cfg.llm_config.embed.name,
            usage={
                "prompt_tokens": 1,
                "total_tokens": 1
            }
        )

