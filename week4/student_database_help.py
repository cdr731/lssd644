import sqlite3 as sq

def sql_ad_hoc_query(CONN:sq.Connection,
               SQL:str):
      
      
      '''
      Accepts:
        SQLite connection
        SQL statement
      Returns:
        cursor
      '''
      pass
      
def sql_execute_query(
          CONN:sq.Connection,
          SQL:str
          ):
    
    '''
    Accepts:
        SQLite connection
        SQL statement 
    '''
    pass
 
def sql_bulk_insert(CONN:sq.Connection,
                    TABLE:str,
                    DATA:list):

#         Accepts:
#         SQLite connection
#         Table to perform inserts 
#         List of dictionaries for multiple row inserts
#         '''

    pass

if __name__ == "__main__":
 
        #Use an in-memory database
        DATABASE_NAME=':memory:'   
        with sq.connect(
            database=DATABASE_NAME
        ) as conn:

                SQL='''CREATE TABLE IF NOT EXISTS dept 
                (deptId INTEGER PRIMARY KEY AUTOINCREMENT,
                dept_name TEXT UNIQUE NOT NULL);'''

                #Create the dept table 
                sql_execute_query(
                    CONN=conn,
                    SQL=SQL
                )

                #insert value into the table  
                sql_bulk_insert(
                    CONN=conn,
                    TABLE='dept',
                    DATA= [
                         {'dept_name':'Finance'},
                         {'dept_name':'HR'} 
                ]                
                )                 
                
                SQL='''SELECT * FROM dept;'''
                rows=sql_ad_hoc_query(
                    CONN=conn,
                    SQL=SQL
                )

                print(f'*'*20)
                if rows:
                    print(f'{rows}')
                print(f'*'*20)

                #Create the employee table
                SQL='''CREATE TABLE IF NOT EXISTS employee 
                (empId INTEGER PRIMARY KEY AUTOINCREMENT,
                emp_name TEXT UNIQUE NOT NULL,
                deptId INTEGER NOT NULL REFERENCES dept(deptId));'''
                
                #Create the dept table 
                sql_execute_query(
                    CONN=conn,
                    SQL=SQL
                )

                #insert value into the table  
                sql_bulk_insert(
                    CONN=conn,
                    TABLE='employee',
                    DATA=[
                         {'emp_name':'Bob','deptId':1},
                         {'emp_name':'Mary','deptId':2} 
                ]                
                )                 
            
                SQL='''SELECT * FROM employee;'''
                rows=sql_ad_hoc_query(
                    CONN=conn,
                    SQL=SQL
                )

                print(f'*'*20)
                if rows:
                    print(f'{rows}')
                print(f'*'*20) 

                SQL='''SELECT 
                    name
                FROM 
                    sqlite_schema
                WHERE 
                    type ='table' AND 
                    name NOT LIKE 'sqlite_%' 
                    ''' 
                          
                cur=sql_ad_hoc_query(CONN=conn,SQL=SQL)
                if cur:
                    print(f'{cur}')
                
                #cast the list of tuples as a set
                #test if the table exists

                #A Python set is the fourth Python
                #collection type
                #A set is unchangeable but you can add and remove
                #items
                #Think of a Python set as a dictionary key without
                #values. Keys are hashed like a dictionary
                #key. They are very performant. I will spare
                #you the math.

                cur_set=set(cur)
                if ('dept',) in cur_set:
                     print(f'Found table')
                else:
                     print(f'Table not found')
