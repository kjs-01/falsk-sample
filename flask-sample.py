from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/login')
def login():
    return 'login page'

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def user(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello_world'))
    print(url_for('user', username='John Doe'))
    print(url_for('login', next='/'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
