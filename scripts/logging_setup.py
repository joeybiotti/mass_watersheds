import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logging():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "pipeline.log")

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s", "%Y-%m-%d %H:%M:%S"
    )

    handler = RotatingFileHandler(log_file, maxBytes=5_000_000, backupCount=3)
    handler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    logging.basicConfig(level=logging.INFO, handlers=[handler, console])
