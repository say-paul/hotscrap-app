from utils import  database


def addUser(mobile_num,name,email,account_type):
    db =  database.Db()
    query = ("INSERT INTO UserProfile (MobileNum,Name,Email,account_type)
              VALUES (mobile_num,name,email,account_type)");
    params = (mobile_num,name,email,account_type )
    return db.insert(query,params)
