import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

data = {'url': 'https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg'}

response = requests.post(url, json=data)

result = requests.post(url, json=data).json()
print(result)