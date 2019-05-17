# Example 04: handling path parameters.
from flask import Flask

app = Flask(__name__)

# Routes can have parameterized paths. Parameters are denoted with angular brackets <>.
# Concrete values, with which resource has been accessed, is passed as a keyword
# argument with the same name.
@app.route('/hello/<name>')
def hello_with_path_param(name):
    return f'Hello, {name}!'

# You can have multiple path parameters in the same route.
@app.route('/<greating>/<name>')
def greeting_with_path_param(greating, name):
    return f'{greating.title()}, {name}!'

@app.route('/integer/<int:x>')
def integer(x):
    return f'You int incremented by one: {x+1}'

if __name__ == '__main__':
    app.run()