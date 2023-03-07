#!/usr/bin/python3
"""
start flask application and display something
"""


from flask import Flask, render_template
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """a route with variable parameters but defult value"""
    try:
        text = text.replace('_', ' ')
    except Exception as e:
        pass
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_it_number(n):
    """adds a varible parameter with a converter to specify it's type"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """render a template if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
