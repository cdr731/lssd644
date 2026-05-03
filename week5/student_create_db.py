import sqlite_helper as sqlh
import sqlite3 as sq3
from dotenv import dotenv_values
import importlib

importlib.reload(sqlh)

if __name__ == "__main__":

    config = dotenv_values(".env_sqlite")
    with sq3.connect(**config) as conn:

        sql = """CREATE TABLE IF NOT EXISTS user (
                    userId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                    user_name TEXT NOT NULL UNIQUE);"""
        sqlh.sql_execute_script(CONN=conn, SQL=sql)

        sql = """INSERT INTO user (user_name) VALUES ('Peter'), ('James'),('John');"""

        sqlh.sql_execute_script(CONN=conn, SQL=sql)

        user = [{'user_name':'Julie'},
                {'user_name':'Becky'},
                {'user_name':'Chris'}]

        sqlh.sql_bulk_insert(CONN=conn, TABLE="user", DATA=user)

        sql = "SELECT * FROM user;"
        results = sqlh.sql_query(CONN=conn, SQL=sql)
        print(f'{results}')