
import flask
import requests

from services.authentication import login_required


ACCESS_TOKEN = 'HbCz3StJHVsP8BfiogAf'

blueprint = flask.Blueprint('gitlab', __name__)

def get_users():

    res = requests.get('http://localhost:8001/api/v4/users', headers={
            'PRIVATE-TOKEN': ACCESS_TOKEN    
    })

    if res.status_code != 200:
        return []

    def fn(u):
        return {
            'email': u.get('email'),
            'name': u.get('name'),
            'status': u.get('state'),
            'is_admin': u.get('is_admin')
        }
    
    return [fn(u) for u in res.json()]

def get_projects():

    res = requests.get('http://localhost:8001/api/v4/projects', headers={
            'PRIVATE-TOKEN': ACCESS_TOKEN    
    })

    if res.status_code != 200:
        return []

    def fn(i):
        return {
            'name': i.get('name'),
            'ssh_link': i.get('ssh_url_to_repo'),
            'owner': i.get('owner').get('name'),
            'path': i.get('path')
        }
    
    return [fn(i) for i in res.json()]

@blueprint.route('/gitlab', methods=['GET'])
@login_required
def gitlab_action():
    context = {
        'route': 'gitlab',
        'users': get_users(),
        'projects': get_projects()
    }
    return flask.render_template('gitlab.html', context=context)