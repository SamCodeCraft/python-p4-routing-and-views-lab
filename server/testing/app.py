#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string route
@app.route('/print/<string:str_param>')
def print_string(str_param):
    print(str_param)
    return f'<h3>Printed String: {str_param}</h3>'

# Count route
@app.route('/count/<int:num>')
def count(num):
    numbers = '\n'.join(str(i) for i in range(num))
    return f'<h3>Counting up to {num}:</h3><pre>{numbers}</pre>'

# Math route
@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "div":
            return str(num1 / num2)
        
    elif operation == "%":
        return str(num1 % num2)
    else:
        return "<h3>Error: Invalid operation</h3>"

if __name__ == '__main__':
    app.run(debug=True)
