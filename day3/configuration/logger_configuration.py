import logging


def configure_logger():
    """Configure and return a logger for the healthcare application."""

    # Create logger
    logger = logging.getLogger("healthcare.logger")
    logger.setLevel(logging.DEBUG)

    # Prevent duplicate logs if root logger is configured elsewhere
    logger.propagate = False

    # Avoid adding multiple handlers on repeated calls
    if logger.hasHandlers():
        return logger

    # Create file handler
    file_handler = logging.FileHandler("healthcare.log", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(file_handler)

    return logger

