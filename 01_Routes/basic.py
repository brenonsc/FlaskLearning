from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/about')
def about():
    return '<h2>About Page</h2>'

@app.route('/user/<username>')
def user(username):
    return '<h2>Hi %s</h2>' % username.capitalize()
         # '<h2>Hi {}</h2>'.format(username.capitalize())

if __name__ == '__main__':
    app.run()