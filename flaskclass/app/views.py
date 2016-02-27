from app import app
from flask import render_template
 
@app.route('/')
def lucky_static():
    lucky_num = 6
    return render_template('simple.html', lucky_num=lucky_num)

@app.route('/tpl/')
def lucky_tpl():
    return render_template('simple.html')