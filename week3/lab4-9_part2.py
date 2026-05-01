# Lab 4-9 Part 2 by Chris Reutz
# import libraries
import mariadb
from tabulate import tabulate
from dotenv import dotenv_values

# configure database
config = dotenv_values(".env_mariadb")
conn = mariadb.connect(**config)

# dictionary of multiple SQL commands
# the key is a description of what the command will display
# the value is the actual SQL command
sql_dict = { 
    "HR tables":"SHOW TABLES FROM HR",
    "dept table":"SELECT * FROM HR.dept",
    "employee table":"SELECT * FROM HR.employee"
}

# show all the tables in HR database and the records in them
with conn.cursor() as curr:
    for sql_desc, sql_cmd in sql_dict.items():
        curr.execute(sql_cmd)
        print(f'Displaying: {sql_desc}')
        print(tabulate(curr, headers='keys', tablefmt='fancy_grid'))
conn.close()