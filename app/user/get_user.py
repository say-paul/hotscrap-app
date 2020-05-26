from utils import  database


def findUserByMob(mobile_num):
    db =  database.Db()
    query = ("SELECT * FROM UserProfile WHERE MobileNum=%s")
    params = (mobile_num, )
    return db.select(query,params)
