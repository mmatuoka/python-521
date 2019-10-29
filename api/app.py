
import flask

from controllers.users import blueprint as users


app = flask.Flask(__name__)

app.register_blueprint(users, url_prefix='/users')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
