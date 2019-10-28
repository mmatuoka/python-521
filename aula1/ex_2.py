
import requests

url = 'https://gen-net.herokuapp.com/api/users'

data = {
    'name': input('Digite seu nome: '),
    'email': input('Digite seu email: '),
    'password': input ('Digite sua senha: ')
}
res = requests.post(url, json=data)

if res.status_code == 200:
    print('Usuário com id {} cadastrado com sucesso'.format(res.json().get('id')))
else:
    print('Erro ao cadastrar usuário\n {}'.format(res.text))