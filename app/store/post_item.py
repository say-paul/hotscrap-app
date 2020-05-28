from utils import database

def addItem(ItemName,ItemUnit,CurrentRate):
    db=database.Db
    query=("INSERT INTO ItemRateChart(ItemName,ItemUnit,CurrentRate) VALUES(%s,%s,%s)")
    params=(ItemName,ItemUnit,CurrentRate)
    return db.select(query,params)