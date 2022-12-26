import requests
import json


URL="http://127.0.0.1:8000/stuinfo/"
''' 
r=requests.get(url=URL)
data=r.json()
print(data)
'''

data={'name':'kabir','roll':202,'city':'chandina'}
json_data=json.dumps(data)

r=requests.post(url=URL,data=json_data)
data=r.json()
print(data)
