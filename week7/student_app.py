from flask import Flask,render_template,url_for,flash,redirect
from datetime import datetime
import sqlite3 as sq
import sqlite_helper as sqlh

if __name__ == "__main__":
   
    app = Flask(__name__)

    @app.route('/')
    @app.route('/users')
    def index():

        title="LIST USERS"
 
        return render_template("student_index.html",
                                current_dt=current_dt,
                                title=title,
                                users=users)
    @app.route('/posts')
    def posts():
          
          
          title="LIST POSTS"
        
          return render_template("student_posts.html",
                                current_dt=current_dt,
                                title=title,
                                posts=posts
                                )

    if __name__ == "__main__":
                 

                db_name=":memory:"
                with sq.connect(database=db_name) as conn:
                    
                    sql_file = 'student_setup_users_and_posts.sql'
                    #open and read the script file
                    with open(file=sql_file,mode='r') as sql_file:
                        sql_script = sql_file.read()

                    #Call the users view    
                    sqlh.sql_execute_script(CONN=conn,SQL=sql_script)
                    sql='''SELECT * FROM vw_users ORDER BY 2'''
                    users=sqlh.sql_query(CONN=conn,
                                           SQL=sql)
                    
                    #Call the posts view
                    sql='''SELECT * FROM vw_posts ORDER BY 3'''
                    posts=sqlh.sql_query(CONN=conn,
                                           SQL=sql) 
                        
                now=datetime.now()
                current_dt=now.strftime("%m/%d/%Y %H:%M")

                app.run(host='0.0.0.0', port=5000, debug=True)

     