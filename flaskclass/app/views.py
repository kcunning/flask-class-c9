from random import randint

from app import app
from flask import render_template
 
@app.route('/')
def lucky_static():
    lucky_num = randint(1, 100)
    return render_template('simple.html', lucky_num=lucky_num)