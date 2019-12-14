import os.path
from os import path
import yaml

class CalcConfig:
    """
    The configuration file parser for the calculator. Raeds the YAML-based
    configuration file if it's present, and supplies sensible defaults if
    not.

    The default confjiguration file location is ``~/.rpn_calc.yaml``, but this
    can be overridden with the constructor.
    """

    def __init__(self, config_file=None):
        """ Instantiate a new CalcConfig object and parse the configuration
        file if present. If the configuration file cannot be found or read,
        default values are supplied and the instance variable ``did_use_defaults``
        is ser to true to indicate this.

        Args:
            config_file (str): The path to the configuration file. Overrides
            the default path and default values if provided and exists.
        """

        DEFAULT_CONFIG_FILE_LOCATION = os.path.expanduser("~/.rpn_calc.yaml")

        if config_file and os.path.exists(config_file):
            self.config_file = config_file
        elif os.path.exists(DEFAULT_CONFIG_FILE_LOCATION):
            self.config_file = DEFAULT_CONFIG_FILE_LOCATION
        else:
            self.config_file = None
        self.did_use_defaults = False

        self.config_values = {}

        if self.config_file:
            self.read_config()
        else:
            self.default_config()


    def default_config(self):
        """Supply default values for the configuration options, in case the
        configuration file is not present."""
        self.config_values = {
            'verbose': False,
            'debug': False,
        }
        self.did_use_defaults = True


    def read_config(self):
        """Read the configuration file if present. If the file is not found
        or is not readable, the default configuration will be used instead.
        """
        try:
            with open(self.config_file) as file:
                self.config_values = yaml.load(file, Loader=yaml.FullLoader)
        except:
            self.default_config()
