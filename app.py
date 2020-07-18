from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/echo/<text>')
def echo(text):
    return escape(text)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
