from utils import database

def updateInfo(ItemName,ItemUnit,CurrentRate,ItemID):
    db= database.Db()
    print("you are updating data for itemid : ")
    print(ItemID)
    query=("UPDATE ItemRateChart set ItemName= %s,ItemUnit=%s,CurrentRate=%s WHERE ItemID=%s")
    params=(ItemName,ItemUnit,CurrentRate,ItemID)
    return db.update(query,params)

