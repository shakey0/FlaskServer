from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="color: SlateBlue; text-align: center;">Hello, World!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
