# Example 05: handling raw POST data.
from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def data():
    # You can access raw POST data with request.data.
    # Note that this is not a string but a bytes object!
    return f'Data that you sent: {request.data}!'

if __name__ == '__main__':
    app.run()