
import flask

from controllers.users import blueprint as users


app = flask.Flask(__name__)

app.register_blueprint(users, url_prefix='/users')

@app.route('/hello-world', methods=[ 'GET'])

def get_hello_world():
    return flask.jsonify({
        'message': 'hello, world'
    })

if __name__ == '__main__':
    app.run()
