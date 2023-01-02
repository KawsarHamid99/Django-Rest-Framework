

import requests
import json

URL="http://127.0.0.1:8000/"

def jsonView(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    json_data=r.json()
    print(json_data)
#jsonView()


def post_data():
    data={'name':'kawsar','roll':115,'city':'khaka'}
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    json_data=r.json()
    print(json_data)

post_data()

def update_data():
    data={'id':2,'name':'ftp',"city":'hulna','roll':'111'}
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)

#update_data()


def delete_data():
    data={'id':7}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)

# delete_data()
