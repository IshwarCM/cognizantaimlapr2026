# configure log format
import logging


def configure_logger():
    """Configure the logger for the healthcare application."""

    """create a logger instance with a specific name and set its level to DEBUG"""
    logger = logging.getLogger("Healthcare Logger")
    logger.setLevel(logging.DEBUG)

    """check if the logger already has handlers to avoid adding 
    multiple handlers in case of multiple calls to this function. """
    if not logger.hasHandlers():
        return logger

    file_handler = logging.FileHandler("healthcare.log")
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
