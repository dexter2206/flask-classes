import json
from operator import add, sub, mul
from flask import Flask, request

app = Flask(__name__)
operators = {'add': add, 'sub': sub, 'mul': mul}

@app.route('/calc', methods=['POST'])
def calc():
    data = request.get_json()
    op = data['op']
    x = data['x']
    y = data['y']
    data['result'] = operators[op](x, y)
    return json.dumps(data)

if __name__ == '__main__':
    app.run()
