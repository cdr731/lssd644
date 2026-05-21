from flask import Flask,render_template,url_for,flash,redirect
from flask import request,jsonify
from datetime import datetime
import sqlite3 as sq
import sqlite_helper as sqlh
from dotenv import dotenv_values
   
app = Flask(__name__)

#ADD TOKEN INFORMATION HERE
config=dotenv_values(".env_jsonify")
secret_jsonify_token=config['secret_key']

@app.route('/')
@app.route('/users')
def index():

    title="LIST USERS"

    return render_template("index.html",
                            current_dt=current_dt,
                            title=title,
                            users=users)
@app.route('/posts')
def posts():  
        
        title="LIST POSTS"
    
        return render_template("posts.html",
                            current_dt=current_dt,
                            title=title,
                            posts=posts
                            )


     
@app.route('/jsonify',methods=['POST'])
def jsonify_api():
     
 #ADD CODE HERE
    data=request.get.get_json()
    if not data:
        return jsonify({"status":"error","message":"No JSON data"}), 400
    
    auth_token = data.get("auth_token")
    if not auth_token:
        return jsonify({"status":"error","message":"No auth_token"}), 401

    if auth_token != secret_jsonify_token:
        return jsonify({"status":"error","message":"Invalid authentication"}), 403
        
    user_payload = data.get("payload", {})
    response_payload = {
        "status":"success",
        "message":"Authentication successful",
        "received_data":user_payload
    }
    return jsonify(response_payload),200

if __name__ == "__main__":
    # config=dotenv_values()
    VALID_SECRET_TOKEN = "super-secret-auth-token"
                
    db_name=":memory:"
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

    app.run(host='0.0.0.0', port=5001, debug=True)

