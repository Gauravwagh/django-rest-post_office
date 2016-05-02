import logging

from .compat import dictConfig


# Taken from https://github.com/nvie/rq/blob/master/rq/logutils.py
def setup_loghandlers(level=None):
    # Setup logging for email if not already configured
    logger = logging.getLogger('email')
    if not logger.handlers:
        dictConfig({
            "version": 1,
            "disable_existing_loggers": False,

            "formatters": {
                "email": {
                    "format": "[%(levelname)s]%(asctime)s PID %(process)d: %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                },
            },

            "handlers": {
                "email": {
                    "level": "DEBUG",
                    "class": "logging.StreamHandler",
                    "formatter": "email"
                },
            },

            "loggers": {
                "email": {
                    "handlers": ["email"],
                    "level": level or "DEBUG"
                }
            }
        })
    return logger
