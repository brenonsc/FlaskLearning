from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Puppies!</h1>'

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    if name[-1] == 'y':
        name = name[:-1] + 'iful'
    else:
        name += 'y'
    return '<h2>Hi %s</h2>' % name.capitalize()

if __name__ == '__main__':
    app.run()