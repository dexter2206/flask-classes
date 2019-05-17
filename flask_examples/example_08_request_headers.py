# Example 01: basic Flask application
from flask import Flask, request

app = Flask(__name__)

@app.route('/headers', methods=['GET'])
def headers():
    print(f'The headers you provided: {request.headers}')
    return f'Your user agent is: {request.headers["User-Agent"]}'

if __name__ == '__main__':
    app.run()
