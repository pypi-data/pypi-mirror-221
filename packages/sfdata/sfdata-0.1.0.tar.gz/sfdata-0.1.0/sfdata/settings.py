import datetime
import logging
import os
import warnings

warnings.filterwarnings("error")


LOGS_DIR = "logs"


def setup_logger():
    logging.captureWarnings(True)

    # Create a logger instance
    logger = logging.getLogger()

    # Get the current date in the format "YYYY-MM-DD"
    current_date = datetime.datetime.now().isoformat()
    if not os.path.exists(LOGS_DIR):
        os.mkdir(LOGS_DIR)

    log_file_path = os.path.join(LOGS_DIR, f"pipeline_{current_date}.log")

    # Create a file handler that logs all messages to a file
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.DEBUG)

    # Create a stream handler that prints log messages to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(
        logging.DEBUG
    )  # Set the level to INFO to only print messages with INFO level or above

    # Create a formatter to format the log messages
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Set the formatter for both handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
