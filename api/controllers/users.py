
import flask

blueprint = flask.Blueprint('users', __name__)

@blueprint.route('/', methods=[ 'GET'])
def get_users():
    return 'get all users'

@blueprint.route('/', methods=[ 'POST'])
def get_users():
    return 'post all users'

@blueprint.route('/<userid>', methods=[ 'GET'])
def get_user_by_id(userid):
    return 'get user with id {}'.format(userid)

@blueprint.route('/<userid>', methods=[ 'PUT'])
def replace_user_by_id(userid):
    return 'put user with id {}'.format(userid)

@blueprint.route('/<userid>', methods=[ 'PATCH'])
def update_user_by_id(userid):
    return 'patch user with id {}'.format(userid)

@blueprint.route('/<userid>', methods=[ 'DELETE'])
def delete_user_by_id(userid):
    return 'delete user with id {}'.format(userid)
