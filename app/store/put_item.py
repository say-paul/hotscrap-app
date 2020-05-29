from utils import database

def updateInfo(ItemId,ItemName,ItemUnit,CurrentRate):
    db= database.Db
    query=("UPDATE ItemRateChart SET ItemName=%s,ItemUnit=%s,CurrentRate=%s WHERE ItemID=%s")
    params=(ItemName,ItemUnit,CurrentRate)
    return db.update(query,params)