from utils import database

def  findItem(ItemID):
    db= database.Db()
    print("the details is : ")
    query=("SELECT * FROM ItemRateChart WHERE ItemID=%s")
    params=(ItemID)
    return db.select(query,params)
