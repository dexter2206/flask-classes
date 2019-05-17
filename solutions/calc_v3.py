from operator import add, sub, mul
from flask import Flask, request

app = Flask(__name__)
operators = {'add': add, 'sub': sub, 'mul': mul}

@app.route('/<op>')
def calc(op):
    x, y = int(request.args['x']), int(request.args['y'])
    return str(operators[op](x, y))

if __name__ == '__main__':
    app.run()
