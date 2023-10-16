# Create a “/welcome” route to display the welcome message “Welcome to ABC Corporation” and
# a “/” route to show the following details:
# Company Name: ABC Corporation,Location: India, Contact Detail: 999-999-9999 

from flask import Flask 

app = Flask(__name__)

@app.route('/')
def details(): 
    return '<h1>Company Name: ABC Corporation</h1> <br> <h1>Location: India</h1> <br> <h1>Contact Detail: 999-999-9999</h1>'

@app.route('/welcome')
def welcome_display():
    return '<h1>Welcome to ABC Corporation</h1>'

if __name__ == '__main__':
    app.run(host = '0.0.0.0')