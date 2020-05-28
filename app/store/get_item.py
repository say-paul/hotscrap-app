from utils import database

def  findItem(ItemID):
    db= database.Db()
    query=("SELECT * FROM ItemRateChart WHERE ItemName=%s")
    params=(ItemID,)
    return db.select(query,params)
