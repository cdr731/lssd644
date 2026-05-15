import sqlite3 as sq

def execute_setup(CONN:sq.Connection,sql_file_name):

    '''This function has to imput arguments:
    db_name | the database name
    sql_file | the sql swcript file name

    5-14-26 daragon@sdccd.edu'''

    #open and read the script file
    with open(file=sql_file_name,mode='r') as sql_file:
        sql_script = sql_file.read()

    try:

        #open a cursor and execute the script
        cursor=CONN.cursor()
        cursor.executescript(sql_script)

    except sq.Error as e:
        print(f'SQL error occured: {e}')

if __name__ == "__main__":

    db_name = ':memory:'
    with sq.connect(database=db_name) as conn:
        sql_file = 'student_setup_users_and_posts.sql'

        execute_setup(CONN=conn,sql_file_name=sql_file)

        cursor=conn.cursor()

        #    CALL THE vw_users VIEW HERE
        cursor.execute("SELECT * FROM vw_users ORDER BY 2")
        rows=cursor.fetchall()
        for row in rows:
            print(f'{row}')

        cursor=conn.cursor()

        # CALL THE vw_posts VIEW HERE
        cursor.execute("SELECT * FROM vw_posts ORDER BY 3")
        rows=cursor.fetchall()
        for row in rows:
            print(f'{row}')
        


