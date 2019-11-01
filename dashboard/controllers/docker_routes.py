
import logging

import flask
import docker

from services.authentication import login_required


blueprint = flask.Blueprint('docker', __name__)

def get_containers():
    try:

        client = docker.DockerClient()

        def fn(c):
            return {
                'id': c.short_id,
                'status': c.status,
                'image': c.image.tags[0] if len(c.image.tags) else "sem tag"
            }

        return [fn(c) for c in client.containers.list(all=True)]

    except docker.errors.DockerException as err:

        logging.error(f'Falha na conexão com o Docker: \n{err}')

        return []

@blueprint.route('/docker', methods=['GET', 'POST'])
@login_required
def docker_route():

    context = {
        'route': 'docker',
        'containers': get_containers()      
    }
    
    return flask.render_template('docker.html', context=context)

@blueprint.route('/docker/<containerid>/start', methods=['GET'])
@login_required
def start_container_action(containerid):

    try:

        client = docker.DockerClient()

        container = client.containers.get(containerid)

        if container:
            container.start()

    except docker.errors.DockerException as err:

        logging.error(f'Falha na conexão com o Docker: \n{err}')

    finally:
        return flask.redirect('/docker')

@blueprint.route('/docker/<containerid>/stop', methods=['GET'])
@login_required
def stop_container_action(containerid):

    try:

        client = docker.DockerClient()

        container = client.containers.get(containerid)

        if container:
            container.stop()

    except docker.errors.DockerException as err:

        logging.error(f'Falha na conexão com o Docker: \n{err}')

    finally:
        return flask.redirect('/docker')