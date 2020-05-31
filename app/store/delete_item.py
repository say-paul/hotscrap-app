from utils import database
def dltItem(ItemID):
    db=database.Db()
    print("You are deleting data for item id : ")
    print(ItemID)
    query=("DELETE FROM ItemRateChart WHERE ItemID=%s")
    params=(ItemID, )
    return db.delete(query,params)

    