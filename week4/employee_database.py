import sqlite3 as sq

def sql_ad_hoc_query(
        CONN:sq.Connection,
        SQL:str
        ):
    '''
    Accepts:
        SQLite connection
        SQL statement
    Returns:
        cursor
    '''
    if SQL:
        cur = CONN.execute(SQL)  
        return(cur.fetchall())     
      
def sql_execute_query(
        CONN:sq.Connection,
        SQL:str
        ):
    '''
    Accepts:
        SQLite connection
        SQL statement 
    '''
    if SQL:
        cur = CONN.execute(SQL)
        CONN.commit()
 
def sql_bulk_insert(
        CONN:sq.Connection,
        TABLE:str,
        DATA:list
        ):
#   Accepts:
#       SQLite connection
#       Table to perform inserts 
#       List of dictionaries for multiple row inserts
#   '''
    if not DATA:
        return
    columns = ', '.join(DATA[0].keys())
    placeholders = ', '.join(['?'] * len(DATA[0]))
    insert_query = f"INSERT INTO {TABLE} ({columns}) VALUES ({placeholders})"
    values = [tuple(data.values()) for data in DATA]
    CONN.executemany(insert_query, values)
    CONN.commit()

if __name__ == "__main__":
 
    #Use an in-memory database
    DATABASE_NAME = ':memory:'   
    with sq.connect(
        database = DATABASE_NAME
        ) as conn:

            SQL = '''CREATE TABLE IF NOT EXISTS dept( 
            deptId INTEGER PRIMARY KEY AUTOINCREMENT,
            dept_name TEXT UNIQUE NOT NULL);'''

            #Create the dept table 
            sql_execute_query(
                CONN = conn,
                SQL = SQL
                )

            #insert value into the table  
            sql_bulk_insert(
                CONN = conn,
                TABLE = 'dept',
                DATA = [
                    {'dept_name':'IT'},
                    {'dept_name':'Finance'},
                    {'dept_name':'Payroll'},
                    {'dept_name':'Development'} 
                    ]                
                )                 
            
            SQL = '''SELECT * FROM dept;'''
            rows = sql_ad_hoc_query(
                CONN = conn,
                SQL = SQL
                )

            print(f'*' * 20)
            if rows:
                print(f'{rows}')
            print(f'*' * 20)

            #Create the employee table
            SQL = '''CREATE TABLE IF NOT EXISTS employee( 
            empId INTEGER PRIMARY KEY AUTOINCREMENT,
            emp_name TEXT UNIQUE NOT NULL,
            deptId INTEGER NOT NULL REFERENCES dept(deptId));'''
            
            #Create the dept table 
            sql_execute_query(
                CONN = conn,
                SQL = SQL
                )

            #insert value into the table  
            sql_bulk_insert(
                CONN = conn,
                TABLE = 'employee',
                DATA = [
                    {'emp_name':'Michael K','deptId':1},
                    {'emp_name':'Karen P','deptId':2},
                    {'emp_name':'Bob H','deptId':1},
                    {'emp_name':'Sarah A','deptId':3},
                    {'emp_name':'Joe W','deptId':4},
                    {'emp_name':'Chris R','deptId':4}    
                    ]                
                )

            SQL = '''SELECT * FROM employee;'''

            rows = sql_ad_hoc_query(
                CONN = conn,
                SQL = SQL
                )

            print(f'*' * 20)
            if rows:
                print(f'{rows}')
            print(f'*' * 20)

            SQL = '''SELECT e.empId, e.emp_name, d.dept_name
            FROM employee AS e
            INNER JOIN dept AS d ON e.deptId = d.deptId
            ORDER BY d.dept_name, e.emp_name;'''
            
            rows = sql_ad_hoc_query(
                CONN = conn,
                SQL = SQL
                )

            print(f'*' * 20)
            if rows:
                print(f'{rows}')
            print(f'*' * 20)

            SQL='''SELECT name FROM sqlite_schema
                WHERE type = 'table' AND 
                name NOT LIKE 'sqlite_%' ''' 
                        
            cur = sql_ad_hoc_query(
                CONN = conn, 
                SQL = SQL
                )

            if cur:
                print(f'{cur}')
            
            #cast the list of tuples as a set
            #test if the table exists
            cur_set = set(cur)
            if ('dept',) in cur_set:
                print(f'Found table')
            else:
                print(f'Table not found')
