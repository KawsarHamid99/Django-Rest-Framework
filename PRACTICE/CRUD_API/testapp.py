import requests
import json


URL="http://127.0.0.1:8000/"
def get_data(id=None):
    data={}
    if id:
        data={'id':id}
    json_data=json.dumps(data)
    headers={'content-type':'application/json'}
    r=requests.get(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(r)
    print(data)




def post_data():
    data={'name':"bablu","roll":55,"city":"Khulna"}
    json_data=json.dumps(data)
    headers={'content-type':'application/json'}

    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)

#post_data()

def put_data():
    data={'id':6,'name':"komola","roll":1212,"city":"Khulna"}
    json_data=json.dumps(data)

    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)

#put_data()


def delete_data():
    data={'id':4,'name':"bakis","roll":1212,"city":"Khulna"}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)

#delete_data()
get_data()