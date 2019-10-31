
import hashlib

import flask
import ldap3

from services.authentication import login_required


blueprint = flask.Blueprint('ldap', __name__)

def get_ldap_connection():
    
    user = 'cn=admin,dc=dexter,dc=com,dc=br'
    password = '4linux'

    try:
        return ldap3.Connection(
            ldap3.Server('ldap://localhost:389'),
            user,
            password,
            auto_bind=True
        )
    except:
        return None

def find_user_by_email(email, conn):
    
    conn.search(
        'uid={},dc=dexter,dc=com,dc=br'.format(email),
        '(objectClass=person)',
        attributes=[
            'sn',
            'userpassword'
        ]
    )
    return conn.entries[0] if len(conn.entries) > 0 else None

def verify_password(user, password):
    
    saved_password = user.userPassword.value.decode()

    return hashlib.sha256(password.encode()).hexdigest() == saved_password

@blueprint.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    
    if flask.request.method == 'POST':

        # pegar objeto da conexão
        conn = get_ldap_connection()

        # extrair as variáveis enviadas pelo usuário
        email = flask.request.form.get('email')
        password = flask.request.form.get('password')

        #encontrar o usuário pelo email no ldap
        user = find_user_by_email(email, conn)

        if user and verify_password(user, password):
            flask.session['authenticated'] = True
            return flask.redirect('/')

    context = {
        'public_route': True
    }
    
    return flask.render_template('ldap.html', context=context)

@blueprint.route('/sign-out', methods=['GET'])
@login_required
def sign_out():
    try:
        del flask.session['authenticated']
    except KeyError:
        pass
    return flask.redirect('/')


