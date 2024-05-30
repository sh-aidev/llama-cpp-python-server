from dotenv import load_dotenv
load_dotenv()

import sys, os
import warnings
warnings.filterwarnings("ignore")

from src.utils.logger import logger
from src import App

def main():
    logger.debug(f"Running main function")
    app = App()
    logger.debug(f"App initialized")
    app.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.debug("Exiting...")
        sys.exit(0)
