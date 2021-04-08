import logging

logger = logging.getLogger(__name__)
print = logger.info


def test():
    print(__name__)
    logger.error(__name__)
