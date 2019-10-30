
import flask


blueprint = flask.Blueprint('docker', __name__)

def fn(i):
    return {
        'id': i,
        'image': f'image {i}',
        'status': 'running'
    }

@blueprint.route('/docker', methods=['GET', 'POST'])
def docker_route():
    
    print(flask.request.form)

    context = {
        'containers': [fn(i+1) for i in range(100)]        
    }
    
    return flask.render_template('docker.html', context=context)