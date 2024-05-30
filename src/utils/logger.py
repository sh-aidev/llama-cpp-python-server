from loguru import logger
import sys, os


# # init logger with custom config
class Logger:
    @staticmethod
    def create_sess(env):
        logger.remove()
        logger.add(
            "outputs/logs/server.log",
            format="{time} {level} {message}",
            rotation="10 MB",
            compression="zip",
            serialize=True,
        )
        env_dict = {"dev": "DEBUG", "prod": "INFO"}
        logger.add(sys.stderr, level=env_dict[env])
        return logger

class Logger_py:

    def __init__(self) -> None:
        self.logger = Logger.create_sess(os.getenv("ENVIRONMENT", 'dev'))
        self.logger.info(
            f"Logger for environemnt: {str(os.getenv('ENVIRONMENT', 'dev'))}"
        )
    
    def run(self) -> Logger:
        return self.logger
        
logger = Logger_py().run()