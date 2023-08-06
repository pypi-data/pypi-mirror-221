try:
    from logging import config
    from django.conf import settings

    config.dictConfig(getattr(settings, "LOGGING", {}))
except:
    config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "simple": {
                    "format": "%(asctime)s (%(process)d:%(thread)d) [%(levelname)s] %(name)s(%(lineno)s): %(message)s"
                }
            },
            "handlers": {
                "console": {
                    "level": "DEBUG",
                    "class": "logging.StreamHandler",
                    "formatter": "simple",
                },
                "file": {
                    "level": "DEBUG",
                    "class": "logging.FileHandler",
                    "formatter": "simple",
                    "filename": "sample.log",
                    "mode": "a",
                },
            },
            "loggers": {
                "": {
                    "handlers": ["console", "file"],
                    "level": "DEBUG",
                    "propagate": True,
                }
            },
        }
    )

import logging


def get_logger(module_name):
    return logging.getLogger(module_name)
