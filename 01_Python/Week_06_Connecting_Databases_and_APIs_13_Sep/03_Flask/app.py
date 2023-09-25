# in this local system we cannot make the our api or url global.
# Now, our computer is only a server.
# here we are trying to execute python function using an url.
from flask import Flask

# object of the flask
app = Flask(__name__)

# this / is a home url 
@app.route("/")
# function is called indirectly i.e through url so we can say it as platform independent.
# so to expose this function on url we use route.
# we will not call the funcion directly if we call it will become language dependent.
# So, here we access through the http protocol.
def home():
    return '<h1>This is home page</h1>'
# to access this function => server -> port number -> then route

@app.route("/test")
def test():
    su = 8 + 4
    return f'This is my first function in flask {su} '

@app.route("/account")
def account():
    return '<h1>This account page</h1>'

# to open we have to open home page then to url we have to add this /hello2 to open this page
@app.route("/order")
def orders():
    return '<h1>This is order page</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
