from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>
            My Dev Dashboard
        </title>
    </head>
    <body>
        <header>
            <h1>
                Welcome to my Dashboard
            </h1>
            <nav>
                <a href="#about">About Me</a>
                <a href="#projects">Current Projects</a>
                <a href="#contact">Contact</a>
            </nav>
        </header>
        <hr>
        <section id="about">
            <h1>About Me</h2>
            <p><strong>I am interested in Python, Flask, DevOPS. </strong> HTML is another part of the puzzle.</p>
            <div>
                <h3>My Projects</h3>
                <ul>
                    <li>
                        Python
                    </li>
                    <li>
                        SQLite3
                    </li>
                </ul>
            </div>
        </section>
        <hr>
        <section id="projects">
        <h2>
            About Me
        </h2>
        <div>
            <ol>
                <li>
                    HTML
                </li>
                <li>
                    <img src="https://flask.palletsprojects.com/en/stable/_images/flask-name.svg" 
                    alt="Flask Logo"
                    width="600"
                    height="400"
                    loading="lazy"
                    title="The Flash logo is a trademarke of Pallets Projects">
                </li>
                <li>
                    Jinja2
                </li>
            </ol>
        </div>
        </section>
        <hr>
        <section id="contact">
            <br>
            <h2>Contact Me</h2>
            <form>
                <p>Subscribe to my newsletter:</p>
                <input type="email" placeholder="Enter your email">
                <button type="submit">Join List</button>
            </form>
        </section>
        <footer>
            <p>&copy; Chris' Web Page</p>
        </footer>
    </body>

    </html>
    '''

if __name__ == "__main__":
    app.run(port=5000, debug=True)


