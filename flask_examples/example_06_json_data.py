# Example 06: handling JSON encoded data
from flask import Flask, request

app = Flask(__name__)

@app.route('/json', methods=['POST'])
def json():
    # If content type of the request is application/json, Flask can
    # automatically decode json object for you.
    # Remember, this will only work if the correct content type is set in the request.
    for key, value in request.get_json().items():
        print(f'{key}: {value}')
    return ''

if __name__ == '__main__':
    app.run()
