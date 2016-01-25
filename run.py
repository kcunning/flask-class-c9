import os

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    # The next two lines are JUST for c9
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    # If you're running on your local, you can nuke stuff in the parens
    app.run(port=port, host=host)
