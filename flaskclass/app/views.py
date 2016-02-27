from app import app
from flask import render_template
 
@app.route('/')
def lucky_static():
    return "Your lucky number is 7"