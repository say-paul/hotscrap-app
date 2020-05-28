import yaml
import os
path = os.path.dirname(os.path.realpath(__file__))
env = os.environ['APP_ENV']

def db_config():
    with open(path + "/env/" + env + ".yml", 'r') as f:
        config = yaml.safe_load(f)
    return config
    