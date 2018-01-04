#coding=utf-8
from flask import Flask
from flask import make_response
from flask import  redirect
import json
from flask import abort

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"

@app.route("/hello")
def do_hello():
    return '<h1>hello stranger!</h1>'

@app.route('/json')
def do_json():
    hello={"name":"stranger","say":"hello"}
    return json.dumps(hello)

@app.route('/status_500')
def status_500():
    return "hello",500

@app.route('/set_header')
def set_header():
    resp = make_response('<h1>This document has a modified header!</h1>')
    resp.headers['X-Something'] = 'A value'
    resp.headers['Server'] = 'My special http'
    return resp

@app.route('/set_cookie')
def set_cookie():
    response = make_response('<h1> This document carries a cookie! </h1>')
    response.set_cookie('username','evancss')
    return response

@app.route('/redir')
def redir():
    return  redirect('http://www.baidu.com')


app.route('/user/<id>')
def get_user(id):
    if int(id)>10:
        abort(404)
    return '<h1>hello,%s</h1>'% id











if __name__=='__main__':
    app.run(debug=True)