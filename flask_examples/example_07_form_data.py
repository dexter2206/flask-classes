# Example 07: handling form data
from flask import Flask, request

app = Flask(__name__)

@app.route('/form', methods=['POST'])
def json():
    # You can access form data using request.form attribute.
    for key, value in request.form.items():
        print(f'{key}: {value}')
    return ''

if __name__ == '__main__':
    app.run()
