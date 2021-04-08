import yaml
from test import test

import logging.config
from utils.logger import setup_logging
logger = logging.getLogger(__name__)
print = logger.info

if __name__ == '__main__':

    print(__name__)  # no output
    with open('./config/main.yaml', "r") as f:
        main_configuration = yaml.load(f, yaml.SafeLoader)
    setup_logging(main_configuration['log']['dir'])
    print(__name__)  # 2021-03-31 11:22:02,902 [INFO] - __main__ : __main__
    test()           # 2021-03-31 11:35:05,002 [INFO] - test : test

