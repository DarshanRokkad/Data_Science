from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def request_input():
    # here we request an arguement and we get the value inside a key x and the input will be stored as a value to the key 'x'
    data = request.args.get('name')
    # http://127.0.0.1:5000/?name=krish
    # give ?variable=value
    return 'Your name is {}'.format(data)
# to url add '?q=input' 
# q is like a parameter

if __name__ == '__main__':
    app.run(host = "0.0.0.0")


# we can pass data to the function through uml , xml , json , url , form ....