# Example 01: basic Flask application
from flask import Flask

# Create an instance of Flask class.
# Instances of Flask class are WSGI applications (more on that later).
app = Flask(__name__)

# Adding routes (think: available paths) boils down to decorating functions with @app.route.
# PATH part of the url as an argument.
# By default, all HTTP methods are supported.
@app.route('/')
def hello_world():
    # Functions decorated with @app.route have to return non-None response.
    # We will see later what kind of objects can be returned, for now we will use strings.
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()