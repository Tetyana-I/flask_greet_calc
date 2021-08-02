# Put your app in here.
from flask import Flask, request 
from operations import add, sub, mult, div

app = Flask(__name__) 

@app.route('/add')
def add_function():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = add(a,b)
    return f"{result}"

@app.route('/sub')
def sub_function():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a,b)
    return f"{result}"

@app.route('/mult')
def mult_function():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a,b)
    return f"{result}"

@app.route('/div')
def div_function():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = div(a,b) if b != 0 else "cannot divide by 0"
    return f"{result}"


OPERATIONS = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<calc>')
def calculation(calc):
    """A single route function that can deal with 4 different operations: add, sub, mult and div"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    func = OPERATIONS.get(calc, "nothing here")
    if func == "nothing here":
        return func
    if calc == "div": 
        if b == 0:
            return "cannot divide by 0"
    result = func(a,b)
    return f"{result}"
