import toml
import os
from src.utils.models import LlamaCppModel

class LLMConfig:

    def __init__(self, root_config_path: str):

        self.llm_config = LlamaCppModel(
            **toml.load(os.path.join(root_config_path, "config.toml"))
        )