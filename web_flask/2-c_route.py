#!/usr/bin/python3
"""
start flask application and display something
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_flask():
    """ return first content """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """another route to hbnb addded"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_isfun(text):
    """a route with a parameter"""
    try:
        text = text.replace('_', ' ')
    except Exception as e:
        pass
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
