import requests
import json

server_url = 'http://192.168.1.181:3000/api/streamproducts'
api_key = 'd'
headers = {
    'Authorization': f'users API-Key {api_key}'
}
response = requests.get(url=server_url,headers=headers)
response.raise_for_status()
print(response.json())

if response.status_code == 200:
    print('response found')
        
else:
    print("Error:", response.status_code)