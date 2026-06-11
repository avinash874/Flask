# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello Flask! This Side is Avinash Singh And Avinash Maurya Both comein from India"

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask
### WSGI - Web Server Gateway Interface Application Programming Interface(API) For Web Server And Web Application To Communicate With Each Other

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome To My flask App.Avinash Sing create This app "

@app.route('/member1')
def welcome1():
    return "Welcome Avinash Singh "

@app.route('/member2')
def welcome2():
    return "Welcome To My country "

if __name__=="__main__":
    app.run(debug=True)