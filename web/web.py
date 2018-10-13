from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def sayhello():
	return 'hello'
@app.route('/hello')
def hello():
    users = [{"username":"users1","url":"/users/user1"},
             {"username":"users2","url":"/users/user2"}]
    return render_template("hello.html",title="User List",users=users)

@app.route('/index')
def index():
	return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)