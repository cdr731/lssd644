import sqlite_helper as sqlh
import sqlite3 as sq3
from dotenv import dotenv_values
import importlib

importlib.reload(sqlh)

if __name__ == "__main__":

    config = dotenv_values(".env_sqlite")
    with sq3.connect(**config) as conn:

        sql = """CREATE TABLE IF NOT EXISTS user (
                    userId INTEGER PRIMARY KEY AUTOINCREMENT, 
                    user_name TEXT NOT NULL);"""
        sqlh.sql_execute_script(conn, sql)

        sql = """INSERT INTO user (userId, user_name) VALUES (1, 'Bob');
                 INSERT INTO user (userId, user_name) VALUES (2, 'Alice');
                 INSERT INTO user (userId, user_name) VALUES (3, 'Mike');"""

        sqlh.sql_execute_script(conn, sql)

        user = [{'user_name':'Peter'},
                {'user_name':'James'},
                {'user_name':'John'}]

        sqlh.sql_bulk_insert(conn, "user", user)

        sql = "SELECT * FROM user;"
        users = sqlh.sql_query(conn, sql)
        print(f'{users}')
