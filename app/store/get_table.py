from utils import database

def getTable():
    db= database.Db()
    print("Request for table")
    query=("SELECT * from ItemRateChart")
    params=()
    return db.select(query,params)