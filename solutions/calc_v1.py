from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def _add():
    return f'{int(request.args["x"]) + int(request.args["y"])}'

@app.route('/sub')
def _sub():
    return f'{int(request.args["x"]) - int(request.args["y"])}'

@app.route('/mul')
def _mul():
    return f'{int(request.args["x"]) * int(request.args["y"])}'

if __name__ == '__main__':
    app.run()