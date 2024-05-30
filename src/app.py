import os
from src.server.server import APIServer
from src.utils.logger import logger
from src.utils.configs import LLMConfig

class App:
    """
    Main application class to run the FastAPI server. This class will initialize the server and run it.
    """
    def __init__(self) -> None:
        root_config_dir = "configs"
        logger.debug(f"Root config dir: {root_config_dir}")
        config = LLMConfig(root_config_dir)
        self.server = APIServer(config)

    def run(self):
        self.server.serve()