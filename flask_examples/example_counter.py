from flask import Flask

count = 0
app = Flask(__name__)

@app.route('/counter')
def counter():
    global count
    count += 1
    return str(count)

if __name__ == '__main__':
    app.run()
