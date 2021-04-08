import yaml
import logging
import logging.config
from pathlib import Path
import pdb


def setup_logging(log_dir='./'):
    """
    Setup logging configuration.
    """
    configuration_path = "./config/logging.yaml"
    with open(configuration_path, "r") as f:
        logging_configuration = yaml.load(f, yaml.SafeLoader)
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    for config in ['info_handler', 'error_handler']:
        filename = logging_configuration['handlers'][config]['filename']
        filename = Path(log_dir).joinpath(filename)
        Path(filename).unlink(missing_ok=True)
        logging_configuration['handlers'][config]['filename'] = filename
    logging.config.dictConfig(logging_configuration)



