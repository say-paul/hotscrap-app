from utils import  database

def getUserByMob(mobile):
    db =  database.Db()
    value = db.getUser(mobile)
    print(value)