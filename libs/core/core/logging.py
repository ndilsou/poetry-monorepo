import logging
import os
import structlog

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
FORMAT = "%(asctime)-15s %(levelname)s %(message)s"
logging.basicConfig(
    format="%(message)s",
    level=logging.getLevelName(LOG_LEVEL),
)

Logger = structlog.stdlib.BoundLogger


def get_logger(name: str) -> Logger:
    """Produces a new logger with the application logging parameter preset.

    Args:
        name (str): name of the logger

    Returns:
        logging.BoundLogger: the new logger
    """
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            # Perform %-style formatting.
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.stdlib.BoundLogger,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )
    logger = structlog.get_logger(name)
    return logger