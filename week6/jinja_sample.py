from flask import Flask,render_template

if __name__ == "__main__":
   
    app = Flask(__name__)

    @app.route('/')
    def index():

        messages=[{'user':"Bob Newhart",
         'content':'The late Bob Newhart starred in the 1970s \'The Bob Newhart Show\' and the 1980s \'Newhart\' sitcoms.'},
         {'user':'Alice Hyatt',
         'content':'Alice Hyatt was a waitress at Mel\'s Diner in the 1970s \'Alice\' sitcom. The character was played by the late Linda Lavin.'},
         {'user':'Betty White',
         'content':'Betty White was an active actress until she passed away before her 100th birthday. Her comedic talent was loved by generations of fans.'},
         {'user':'Chris Reutz',
         'content':'I know what you are thinking: \'He is not a celebrity.\' Yes, you are right. But if I could be a character, I would be R2-D2!'}
        ]
        
        page_name="Chris\' Celebrity Main Page"
        page_title="Chris\' Celebrity Site"

        return render_template("test.html",
                               page_name=page_name,
                               page_title=page_title,
                               messages=messages)
        
    if __name__ == "__main__":   
        app.run(host='0.0.0.0', port=5000, debug=True)