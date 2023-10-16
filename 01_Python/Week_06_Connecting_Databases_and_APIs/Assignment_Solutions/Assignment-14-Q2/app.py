# Q.Create a simple Flask application to display ‘Hello World!!’.

from flask import Flask 

app = Flask(__name__)

@app.route('/')
def display():
    return '<h1>Hello World</h1>'

if __name__ == '__main__':
    app.run(host = '0.0.0.0')