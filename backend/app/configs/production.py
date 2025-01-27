# backend/app/configs/production.py

import yaml

with open('configs/production.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

DATABASE_CONFIG = config['database']
SERVER_CONFIG = config['server']
SECRET_KEY = config['secret_key']
LOGGING_CONFIG = config['logging']

DEBUG = False