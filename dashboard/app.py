
import os

import flask
import dotenv

from controllers.docker import blueprint as docker
from controllers.gitlab import blueprint as gitlab
from controllers.jenkins import blueprint as jenkins
from controllers.ldap import blueprint as ldap


dotenv.load_dotenv()

app = flask.Flask(__name__)

app.secret_key = os.environ.get('SECRET KEY') or 'secret'

app.register_blueprint(docker)
app.register_blueprint(gitlab)
app.register_blueprint(jenkins)
app.register_blueprint(ldap)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

