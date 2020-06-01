from utils import database

def updateInfo(ItemName,ItemUnit,CurrentRate,ItemID):
    db= database.Db()
    print("you are updating data for itemid : ")
    print(ItemID,ItemName,ItemUnit,CurrentRate)
    params={"ItemName" : ItemName,"ItemUnit" : ItemUnit,"CurrentRate": CurrentRate}
    d="UPDATE ItemRateChart set "
    for key in params:
        print(key)
        if params[key]!= None:
            d+=key+"="+str(params[key])+" "
    d+="WHERE ItemID = {}".format(ItemID)
    query='("'+d+'")'
    print(query)
    return db.update(query,params)

