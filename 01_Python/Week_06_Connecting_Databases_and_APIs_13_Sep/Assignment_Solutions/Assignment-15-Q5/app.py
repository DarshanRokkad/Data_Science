from flask import Flask , request , jsonify

app = Flask(__name__)

@app.route('/api_testing', methods = ['POST'])
def calculate():
    operation = request.json['operation']
    num1 = int(request.json['num1'])
    num2 = int(request.json['num2'])
    if operation == 'add':
        result = str(num1) + ' + ' + str(num2) + ' = ' + str(num1 + num2)
    if operation == 'sub':
        result = str(num1) + ' - ' + str(num2)+ ' = ' + str(num1 - num2)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host = '0.0.0.0')