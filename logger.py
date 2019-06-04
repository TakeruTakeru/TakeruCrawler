from logging import (
    getLogger, DEBUG, FileHandler, StreamHandler,
    Formatter
    )
from constants.base import LOG_PATH, LOG_FORMAT

logger = getLogger(__package__)
logger.setLevel(DEBUG)
file_handler = FileHandler(LOG_PATH)
stream_handler = StreamHandler()
stream_handler.setLevel(DEBUG)
formatter = Formatter(LOG_FORMAT)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)