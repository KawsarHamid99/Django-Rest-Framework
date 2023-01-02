

import requests
import json

URL="http://127.0.0.1:8000"

def jsonView(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    headers={'content-type':'application/json'}
    r=requests.get(url=URL,headers=headers,data=json_data)
    json_data=r.json()
    print(json_data)
#jsonView()


def post_data():
    data={'name':'turin','roll':194,'city':'Dhaka'}
    json_data=json.dumps(data)
    headers = {'content-type':'application/json'}
    r=requests.post(url=URL,headers=headers,data=json_data)
    json_data=r.json()
    print(json_data)

#post_data()

def update_data():
    data={'id':3,"city":'khulna','roll':'111'}
    json_data=json.dumps(data)
    headers={"content-type":"application/json"}
    r=requests.put(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

#update_data()


def delete_data():
    data={'id':3}
    json_data=json.dumps(data)
    headers={"content-type":"application/json"}
    r=requests.delete(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

#delete_data()
