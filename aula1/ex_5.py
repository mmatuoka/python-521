
import requests

import ex_4

url = 'https://gen-net.herokuapp.com/api/users'

def change_password(user):
    user.update({
        'password': input('Digite a nova senha: ')
    })

    res = requests.put(url + '/' + str(user.get('id')), json=user)

    if res.status_code == 200:
        return True

    return False

if __name__ == "__main__":

    email = input('Digite seu email: ')

    user = ex_4.get_user_by_email(email)

    if user:
        change_password(user)
        print('Senha alterada com sucesso!')
    else:
        print('usuário não encontrado')