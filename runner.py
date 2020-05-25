import os
import sys
path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path + '/')
sys.path.append(path + '/app/')
from routes import app
import yaml
global DB_CONFIG
env = os.environ['APP_ENV']
with open(path+"/env/"+env+".yml", 'r') as f:
    DB_CONFIG = yaml.safe_load(f)


if __name__ == "__main__":
    app.run()