
import requests

url = 'https://gen-net.herokuapp.com/api/users'

data = {
    'email': 'mmatuoka@hotmail.com'
}

res = requests.get(url, params=data)

if res.status_code == 200:
    print(res.json())
else:
    print(res.text)
