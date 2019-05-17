from flask import Flask, request

app = Flask(__name__)

@app.route('/<op>')
def calc(op):
    x, y = int(request.args['x']), int(request.args['y'])
    if op == 'add':
        return f'{x+y}'
    elif op == 'sub':
        return f'{x-y}'
    elif op == 'mul':
        return f'{x*y}'

if __name__ == '__main__':
    app.run()
