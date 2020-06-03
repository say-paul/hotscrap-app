from utils import database


def updateInfo(ItemID,ItemName=None, ItemUnit=None, CurrentRate=None):
    db= database.Db()
    print("you are updating data for id : {}".format(ItemID))
    print(ItemName,ItemUnit,CurrentRate)
    args={"ItemName" : ItemName,"ItemUnit" : ItemUnit,"CurrentRate": CurrentRate}
    query="UPDATE ItemRateChart set "
    params = ()
    for key in args:
        if args[key]!= None:
            query += key + "=" + "%s "
            params += (args[key], )
    query += "WHERE ItemID=%s"
    params += (ItemID,)
    return db.update(query,params)
