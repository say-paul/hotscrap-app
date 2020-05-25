import os
import sys
path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path+'/')
sys.path.append(path+'/app/')

from utils import database
from user import getUser

getUser.getUserByMob("9804123184")