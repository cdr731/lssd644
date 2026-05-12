from flask import Flask,render_template

if __name__ == "__main__":
   
    app = Flask(__name__)

    @app.route('/')
    def index():

        messages=[{'user':"Bob",
         'content':'Message One'},
         {'user':'Alice','content':'Message Two'},
         {'user':'Betty','content':'Betty\'s recipe of the day'}]
        
        page_name="Messages Page"
        page_title="Messages Title"

        return render_template("test.html",
                               page_name=page_name,
                               page_title=page_title,
                               messages=messages)
        
    if __name__ == "__main__":   
        app.run(host='0.0.0.0', port=5000, debug=True)