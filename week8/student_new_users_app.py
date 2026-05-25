# Lab 8 assignment by Chris Reutz
# The main application for users and posts

from flask import Flask,render_template,url_for,flash,redirect
from flask import request,jsonify
from datetime import datetime
import sqlite3 as sq
import sqlite_helper as sqlh
from dotenv import dotenv_values
   
app = Flask(__name__)

#intialize the .env file variable
config=dotenv_values(".env_jsonify")
app.secret_key=config['secret_key'] #required to prevent CSRF attack
db_name=config['db_name']
secret_jsonify_token=config['secret_key']

@app.route('/')
@app.route('/users')
def index():
        
        with sq.connect(database=db_name) as conn:

            #Refresh the users view    
            sqlh.sql_execute_script(CONN=conn,SQL=sql_script)
            sql='''SELECT * FROM vw_users ORDER BY 2'''
            users=sqlh.sql_query(CONN=conn,
                                    SQL=sql)

        title="LIST USERS"
        return render_template("index.html",
                                current_dt=current_dt,
                                title=title,
                                users=users)

@app.route('/posts')
def posts():  

        #Call the posts view
        with sq.connect(database=db_name) as conn:
            #Refresh the posts view    
            sqlh.sql_execute_script(CONN=conn,SQL=sql_script)
            sql='''SELECT * FROM vw_posts ORDER BY 3'''
            posts=sqlh.sql_query(CONN=conn,
                                    SQL=sql)

        title="LIST POSTS"
        return render_template("posts.html",
                            current_dt=current_dt,
                            title=title,
                            posts=posts
                            )

#Add new user
@app.route('/new_user',methods=['GET'])
def add_user_page():
    title="New User"
    return render_template('add_user.html',current_dt=current_dt,title=title)

@app.route('/new_user',methods=['POST'])
def add_user():
    username=request.form.get('user_name').strip()
    if not username:
        flash('Please provide a new username')

    with sq.connect(database=db_name) as conn:
        try:
            conn.execute(
                "INSERT INTO user (user_name) VALUES (?)",(username,)
            )
            conn.commit()
            flash(f"User has been successfully added {username}","success")
        
        except sq.IntegrityError:
            flash(f"Duplicate user {username}")    
    
    return redirect(url_for("index"))
#end of add user section

# Add new post
@app.route('/new_post',methods=['GET'])
def add_post_page():
    title="New Post"
    return render_template('add_post_page.html',current_dt=current_dt,title=title)

@app.route('/new_post',methods=['POST'])
def add_post():
    usrid=request.form.get('userId').strip()
    postmsg=request.form.get('post_message').strip()
    if not usrid:
        flash('Please provide a user Id')
    if not postmsg:
        flash('Please provide a post message')

    with sq.connect(database=db_name) as conn:
        try:
            conn.execute(
                "INSERT INTO blog_posts (userId, post_message) VALUES (?, ?)",(usrid, postmsg)
            )
            conn.commit()
            flash(f"Post message successfully added","success")
        
        except sq.IntegrityError:
            flash(f"Both a user Id or post message are required")    
    return redirect(url_for("posts"))
#end of and post section
    
@app.route('/jsonify',methods=['POST'])
def jsonify_api():
     
    #Get the data
    data = request.get_json()
    #Verify we have data
    if not data:
        return jsonify({"status":"error","message":"No JSON data"}), 400
     
    #Retrieve the aut_token
    auth_token =data.get("auth_token")
    #Verify that the token has been retrieved
    if not auth_token:
        return jsonify({"status":"error","message":"No auth_token"}), 401
     
    #Verify the submitted auth_token is valid
    if auth_token != secret_jsonify_token:
       return jsonify({"status":"error","message":"Invalid authentication"}), 403
     
    #Call the users view 


    #Return a payload response to client
    user_payload = data.get("payload",{})
    response_payload = {
        "status":"success",
        "message":"Authentication successful",
        "user_data":users,
        "received_data":user_payload
    }
    return jsonify(response_payload),200

if __name__ == "__main__":
    print(f'{db_name}')
        
    with sq.connect(database=db_name) as conn:
        
        sql_file = 'setup_users_and_posts.sql'
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
