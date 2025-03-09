from flask import Flask, jsonify
import re
import sympy as sp

app = Flask(__name__)

def evaluate_expression(expr):
    try:
        # Replace '^' with '**' for exponentiation
        expr = expr.replace("^", "**")
        
        # Validate input using regex to allow functions like diff, integrate, sin, cos, log, etc.
        if not re.match(r'^[0-9a-zA-Z+\-*/().^, ]+$', expr):
            return "Invalid characters in expression"
        
        # Check if expression contains functions or just arithmetic
        if any(func in expr for func in ["sin", "cos", "tan", "log", "diff", "integrate"]):
            result = eval("sp." + expr, {"sp": sp, "x": sp.Symbol('x')})
        else:
            result = sp.sympify(expr)
        
        # Convert logs and other functions to numerical values where applicable
        result = result.evalf() if isinstance(result, sp.Expr) else result
        
        return float(result) if result.is_real else str(result)
    except Exception as e:
        return str(e)

@app.route('/<path:expression>', methods=['GET'])
def calculate(expression):
    result = evaluate_expression(expression)
    return jsonify({"expression": expression, "result": result})

@app.route('/')
def index():
    return "This is a simple calculator API. Use the URL to input a mathematical expression."

if __name__ == '__main__':
    app.run(debug=True)
