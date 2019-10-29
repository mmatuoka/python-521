
import flask

from models.user import User


blueprint = flask.Blueprint('users', __name__)

@blueprint.route('/', methods=[ 'GET'])
def get_users():
    users = User.get_all_users()

    return flask.jsonify([u.to_json() for u in users])

@blueprint.route('/', methods=[ 'POST'])
def get_post_users():

    required_fields = ['name', 'email', 'password']

    for field in required_fields:
        if field not in flask.request.json:
            return flask.jsonify({
                'error': f'{field} is required'
            }), 400
    user = User(**flask.request.json)

    if User.find_by_email(user.email):
        return flask.jsonify({
            'error': 'email already exists'
        }), 400

    user.save()

    return flask.jsonify(User.find_by_email(user.email).to_json())

@blueprint.route('/<userid>', methods=[ 'GET'])
def get_user_by_id(userid):

    user = User.find_by_id(userid)

    if not user:
        return flask.jsonify({
            'error': 'user not found'
        }), 404

    return flask.jsonify(user.to_json())

@blueprint.route('/<userid>', methods=[ 'PUT'])
def replace_user_by_id(userid):

    user = User.find_by_id(userid)

    if not user: 
        return flask.jsonify({
            'error': 'user not found'
    }), 404

    email = flask.request.json.get('email')

    if email and User.find_by_email(user.email):
        return flask.jsonify({
            'error': 'email already exists'
        }), 400
    
    opts = {
        'id': user._id,
        'name': None,
        'email': None,
        'password': None
    }
    opts.update(**flask.request.json)

    user = User(**opts)

    user.save()

    return flask.jsonify(
        User.find_by_id(userid).to_json()
    )

@blueprint.route('/<userid>', methods=[ 'PATCH'])
def update_user_by_id(userid):

    user = User.find_by_id(userid)

    if not user:
        return flask.jsonify({
            'error': 'user not found'
    }), 404

    email = flask.request.json.get('email')

    if email and User.find_by_email(user.email):
        return flask.jsonify({
            'error': 'email already exists'
        }), 400
    
    opts = {
        'id': user._id,
        'name': user.name,
        'email': user.email,
        'password': user.password
    }
    opts.update(**flask.request.json)

    user = User(**opts)

    user.save()

    return flask.jsonify(
        User.find_by_id(userid).to_json()
    )

    
@blueprint.route('/<userid>', methods=[ 'DELETE'])
def delete_user_by_id(userid):

    user = User.find_by_id(userid)

    if not user:
        return flask.jsonify({
            'error': 'user not found'
        }), 404

    user.remove()

    return flask.jsonify(user.to_json())
