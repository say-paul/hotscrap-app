from utils import database
def dltItem(ItemID):
    db=database.Db
    query=("DELETE FROM ItemRateChart WHERE ItemID=%s")
    params=(ItemID)
    return db.select(query,params)