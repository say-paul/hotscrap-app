import mysql.connector as mariadb

class Db:
    def __init__(self):
        self.mariadb_connection = mariadb.connect(user='djangouser',
        password='lemongrass', database='hotscrap')
        self.cursor = self.mariadb_connection.cursor()

    def getUser(self,mobileNum):
        query = ("SELECT * FROM UserProfile WHERE MobileNum=%s")
        try:
            print(query)
            self.cursor.execute(query, (mobileNum,))
        except mariadb.Error as error:
            print("Error: {}".format(error))
            return ""
        return self.cursor.fetchone()