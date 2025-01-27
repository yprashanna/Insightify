# backend/app/configs/testing.py

import yaml

with open('configs/testing.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

DATABASE_CONFIG = config['database']
SERVER_CONFIG = config['server']
SECRET_KEY = config['secret_key']
LOGGING_CONFIG = config['logging']

DEBUG = False