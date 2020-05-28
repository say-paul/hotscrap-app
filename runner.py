import os
import sys
path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path + '/')
sys.path.append(path + '/app/')
from routes import app
import yaml

if __name__ == "__main__":
    app.run()
    