import re
import requests
import json

URL="http://127.0.0.1:8000/"
def create_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)

#create_data()

def post_data():
    data={
        'id':2,
        'name':'kabila',
        'roll':104,
        'dept':"ME"
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)
post_data()

def update_data():
    data={ 
        'id':3,
        'name':'sakib',
        'roll':2001,
        'dept':"ENGLISH",
    }

    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)
#update_data()

def delete_data():
    data={'id':4}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)
#delete_data()
