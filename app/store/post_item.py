from utils import database

def addItem(ItemID,ItemName,ItemUnit,CurrentRate):
    db=database.Db
    query=("INSERT INTO ItemRateChart (ItemID,ItemName,ItemUnit,CurrentRate) VALUES(%s,%s,%s,%s)")
    params=(ItemID,ItemName,ItemUnit,CurrentRate)
    return db.insert(query, params)
