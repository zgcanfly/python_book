#coding:utf-8

from flask import *

app=Flask(__name__)

@app.route('/')
def root():
    return jsonify('wecome to root')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__=='__main__':
    app.run()