# Lab 7-9 assignment by Chris Reutz
# Sqlite helper module

from dotenv import dotenv_values
from datetime import datetime
from tabulate import tabulate
import sqlite3 as sq
import json

def sql_query(CONN:sq.Connection, SQL:str):

    """
    Modified daragon@sdccd.edu
    DAte: 4-30-2026

    This function processes a SQL query and returns a cursor.

    Accepts:
        sqlite connection
        SQL query string
    Returns:
        cursor"""

    if CONN:
        try:
            cursor = CONN.cursor()
            cursor.execute(SQL)
            # CONN.commit()
        except sq.Error as e:
            print(e)

        return cursor.fetchall()
    
def sql_execute_query(CONN:sq.Connection, SQL:str):

    """
    Modified daragon@sdccd.edu
    DAte: 4-30-2026
    
    This function processes a SQL query and commits change.
    to a database. It does not return a cursor.

    Accepts:
        sqlite connection
        SQL query string
    Returns:
       None"""
    
    if CONN:
        try:
            cursor = CONN.cursor()
            cursor.execute(SQL)
            CONN.commit()
        except sq.Error as e:
            print(e)

def sql_execute_script(CONN:sq.Connection, SQL:str):

    """
    Modified daragon@sdccd.edu
    DAte: 4-30-2026
    
    This function excutes a SQL statements, commits changes a 
    datebase/table and does not return a cursor.

    Accepts:
        sqlite connection
        SQL statements
    Returns:
        None"""

    if CONN:
        try:
            cursor = CONN.cursor()
            cursor.executescript(SQL)
            CONN.commit()
        except sq.Error as e:
            print(e)

def sql_bulk_insert(CONN:sq.Connection, TABLE:str, DATA:list):
    """
    Modified daragon@sdccd.edu
    Date: 4-30-2026

    This function inserts multiple rows into a table.

    Accepts:
        sqlite connection
        table name
        list of dictionaries containing data for each row
    Returns:
        None"""
    
    if CONN and TABLE and DATA:
        columns = ', '.join(DATA[0].keys())
        placeholders = ', '.join(['?'] * len(DATA[0]))
        insert_sql = f"INSERT INTO {TABLE} ({columns}) VALUES ({placeholders})"
        values = [tuple(row.values()) for row in DATA]
        try:
            CONN.executemany(insert_sql, values)
            CONN.commit()
     
        except sq.Error as e:
            print(e)


def get_host_info():
     
     
     '''
     Function has no argument and returns a string of JSON data
        about the platform and host
     '''

    #import standard libraries to 
    #gather information about
    #the hardware & software platform
    #------------------------
     from socket import gethostname
     from socket import gethostbyname
     from platform import platform
     from platform import processor
     from platform import python_version_tuple
     from os import getcwd
    #------------------------

    #Build a JSON structure to store plaform information

     sys_info = {}
     sys_info['ip'] = gethostbyname(gethostname())
     sys_info['platform'] = platform()
     sys_info['processor'] = processor()
     sys_info['current_dir'] = getcwd()
     sys_info['python_ver'] = python_version_tuple()
     info={"host":sys_info}

     #Return JSON data
     return (json.dumps(info))

if __name__ == '__main__':
        
   
    db =  dotenv_values(".env_sqlite")
    # print(f"Using database: {db}")
    with sq.connect(**db) as conn:

        #create the user table
        sql="""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL);"""
        sql_execute_script(conn, sql)

        #insert some users
        sql="""INSERT INTO users (user_name) VALUES ('Peter'), ('Paul'), ('John');"""
        sql_execute_script(conn, sql)
        
        #test bulk insert
        users=[{"user_name": "Alice"}, {"user_name": "Bob"}]
        sql_bulk_insert(conn, "users", users)

        #query the users
        sql="""SELECT * FROM users;"""
        result_set=sql_query(conn, sql)
        print(tabulate(result_set, headers=['id', 'user_name'], tablefmt='psql'))

        data=get_host_info()
        print(data)