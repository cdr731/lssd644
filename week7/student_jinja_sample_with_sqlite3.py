from flask import Flask,render_template
from datetime import datetime
import sqlite3 as sq
import sqlite_helper as sqlh

if __name__ == "__main__":
   
    app = Flask(__name__)

    @app.route('/')
    def index():

        # messages=[{'user':"Bob",
        #  'content':'Message One'},
        #  {'user':'Alice','content':'Message Two'},
        #  {'user':'Betty','content':'Betty\'s recipe of the day'}]
        
        db_name=":memory:"
        with sq.connect(database=db_name) as conn:

            #Create a table
            sql = '''CREATE TABLE IF NOT EXISTS user (userId INTEGER PRIMARY KEY AUTOINCREMENT, user_name TEXT NOT NULL)'''
            sqlh.sql_execute_query(CONN=conn,
                                   SQL=sql)
            # #Create a view
            # sql='''CREATE VIEW IF NOT EXISTS vw_users as SELECT userId AS Id, user_name AS User' FROM user'''
            # sqlh.sql_execute_query(CONN=conn,
            #                        SQL=sql)
            
            #Query for a row
            sql='''SELECT * FROM user ORDER BY 2 LIMIT 1'''
            one_row = sqlh.sql_query(CONN=conn,
                                   SQL=sql)
            
            #Check if there are already rows in the recordset don't insert
            if not one_row:
                sql='''INSERT INTO user (user_name) VALUES ('Bob'),('Alice'),('Mickey'),('Chris')'''
                sqlh.sql_execute_query(CONN=conn,
                                    SQL=sql) 

            #Call the users tto pass to the webpage    
            sql='''SELECT * FROM user ORDER BY 2'''
            users=sqlh.sql_query(CONN=conn,
                                   SQL=sql)
                                 
        page_name="Display Users"
        page_title="LIST USERS"
        loop_title="USERS"
        now=datetime.now()
        current_dt=now.strftime("%m/%d/%Y %H:%M")

        return render_template("student_list_users.html",
                                page_title=page_title,
                                page_name=page_name,
                                loop_title=loop_title,
                                current_dt=current_dt,
                                users=users)
        
    if __name__ == "__main__": 

        app.run(host='0.0.0.0', port=5000, debug=True)