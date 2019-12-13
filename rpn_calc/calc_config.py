import os.path
from os import path
import yaml

class CalcConfig:

    def __init__(self, config_file=None):
        if config_file and os.path.exists(config_file):
            self.config_file = config_file
        elif os.path.exists(os.path.expanduser("~/.rpn_calc.yaml")):
            self.config_file = os.path.expanduser("~/.rpn_calc.yaml")
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
