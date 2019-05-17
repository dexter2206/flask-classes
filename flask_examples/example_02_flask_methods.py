# Example 02: restricting allowed methods.
# This example is accompanied by an example in requests_example.
from flask import Flask, request

app = Flask(__name__)

# Adding list of methods in @app.route results in restricting given
# route. For other methods, 405 "not allowed" status page will be
# generated.
@app.route('/both', methods=['GET', 'POST'])
def example_both():
    return f'{request.path} requested with {request.method} method.'

@app.route('/get', methods=['GET'])
def example_get():
    return f'{request.path} requested with {request.method} method.'

@app.route('/post', methods=['POST'])
def example_post():
    return f'{request.path} requested with {request.method} method.'

if __name__ == '__main__':
    app.run()