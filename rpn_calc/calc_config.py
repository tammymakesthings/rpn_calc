import os.path
from os import path
import yaml

"""
.. class:: CalcConfig
   :synopsis: Parses the calculator configuration file and sets options,
              or provides defaults if the configuration file is not found.

.. moduleauthor:: Tammy Cravit <tammymakesthings@gmail.com
"""
class CalcConfig:

    DEFAULT_CONFIG_FILE_LOCATION = os.path.expanduser("~/.rpn_calc.yaml")

    def __init__(self, config_file=None):
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
        self.config_values = {
            'verbose': False,
            'debug': False,
        }
        self.did_use_defaults = True

    def read_config(self):
        try:
            with open(self.config_file) as file:
                self.config_values = yaml.load(file, Loader=yaml.FullLoader)
        except:
            self.default_config()
