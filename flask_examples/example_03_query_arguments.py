# Example 03: Handling query arguments.
from flask import Flask, request

# The "request" object imported above holds global information on current request.

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    # request.args is a mapping containing passed query arguments.
    # It behaves like a dictionary - be aware of possible KeyErrors!
    name = request.args['name']
    return f'Hello, {name}!'

@app.route('/hello2')
def hello_world2():
    # As usually with a dict, you can use get method and pass additional default value.
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()