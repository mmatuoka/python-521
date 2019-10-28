
import requests

import ex_4

url = 'https://gen-net.herokuapp.com/api/users'

def verify_password(email, password, user):
    res = requests.post(url + '/auth', {
        'email': email,
        'password': password
    })
    
    return res.status_code == 200

def delete_user(user):
    requests.delete(url + '/' + user.get('id'))

if __name__ == "__main__":

    email = input('Digite seu email: ')

    password = input('Digite sua senha: ')
    
    user = ex_4.get_user_by_email(email)

    if user and verify_password(email, password, user):
        delete(user)
        print('Usuário removido com sucesso!')
    else:
        print('Falha na operação')