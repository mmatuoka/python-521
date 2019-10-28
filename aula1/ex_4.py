
import requests

url = 'https://gen-net.herokuapp.com/api/users'

def get_user_by_email(email):
    res = requests.get(url, params={
        'email': email
    })

    if res.status_code == 200:
        try:
            return res.json()[0]
        except IndexError:
            pass

        return None

if __name__ == "__main__":

    email = input('Digite seu email: ')

    user = get_user_by_email(email)

    if user:
        print(user.get('name'))
    else:
        print('usuário não encontrado')

    