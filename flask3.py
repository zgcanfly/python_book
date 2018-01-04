from flask import Flask,render_template
app = Flask(__name__) 

@app.route('/hello')
def hello():
    users = [{"username":"users1","url":"/users/user1"},
             {"username":"users2","url":"/users/user2"}]
    return render_template("hello.html",title="flask python",users=users)

if __name__ == '__main__':
    app.run(debug=True)
