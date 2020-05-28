import mysql.connector as mariadb
from config import db_config

class Db:
    def __init__(self):
        DB_CONFIG = db_config()
        self.mariadb_connection = mariadb.connect(
            host=DB_CONFIG['db_host'],
            port=DB_CONFIG['db_port'],
            user=DB_CONFIG['db_username'],
            password=DB_CONFIG['db_password'],
            database='hotscrap')
        self.cursor = self.mariadb_connection.cursor()

    def select(self,query,params):
        try:
            self.cursor.execute(query, params)
        except mariadb.Error as error:
            print("Error: {}".format(error))
            return ""
        return self.cursor.column_names, self.cursor.fetchall()

    def insert(self,query,params):
        try:
            self.cursor.execute(query, params)
            print(self.cursor.rowcount, "record inserted.")
        except mariadb.Error as error:
            print("Error: {}".format(error))
            return True
        self.mariadb_connection.commit()
        return self.cursor.lastrowid
        