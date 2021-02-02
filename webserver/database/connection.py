from DataBaseManager import sqlite

DB = "./database/database.db"

try:
    MyObj = sqlite(DB)
    MyObj.CreateDb(f"{DB}", {"users":{"column":"string"}})
except Exception as err:
    print(err, __file__)