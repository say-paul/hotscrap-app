from utils import  database


def addUser(mobile_num,name,email,account_type):
    db =  database.Db()
    print("Inserting the following data:")
    print(mobile_num, name, email, account_type)
    query = ("INSERT INTO UserProfile (MobileNum,Name,Email,account_type) VALUES (%s,%s,%s,%s)")
    params = (mobile_num,name,email,account_type,)
    return db.insert(query,params)
