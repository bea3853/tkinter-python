import requests

url = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(url)

if response.status_code == 200:
  
    data = response.json()


    for user in data:
        print(f"Nome: {user['name']}, Email: {user['email']}")
else:
        print(f"A solicitação falhou com código de status {response.status_code}")


