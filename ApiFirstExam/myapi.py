import requests 
import json


URL="http://127.0.0.1:8000/"

def show(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    json_data=r.json()
    print(json_data)
show()

def create():
    data={"name":"bakis","roll":4102,"city":"Khulna"}
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    json_data=r.json()
    print(json_data)
#create()


def update():
    data={"id":5,"name":"nadia","city":"chandpur"}
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    json_data=r.json()
    print(json_data)
#update()


def delete():
    data={"id":6}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    json_data=r.json()
    print(json_data)
#delete()