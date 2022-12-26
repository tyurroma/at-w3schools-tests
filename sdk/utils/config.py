import configparser
import os
from pathlib import Path


class Config:

    @staticmethod
    def get_variable(variable_name, config_section=None):
        if not variable_name:
            raise TypeError('Variable name is not defined')

        value = os.getenv(variable_name, None)
        if value:
            return value
        else:
            if not config_section:
                raise TypeError('Config section is not defined')

            settings = configparser.ConfigParser()
            settings_filepath = Path('settings.ini')
            settings.read(settings_filepath)
            if config_section in settings and variable_name in settings[config_section]:
                return settings[config_section][variable_name]
            else:
                raise TypeError(f'Variable with name "{variable_name}" not exists in {settings_filepath}')
