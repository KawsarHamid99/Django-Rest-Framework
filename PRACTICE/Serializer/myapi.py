import requests
import json
URL="http://127.0.0.1:8000/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    headers={'content-type':'application/json'}
    r=requests.get(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(f"data---->> {data}")

#get_data()

def post_data():
    data={"name":"kobita","roll":2260,"dept":"FISH"}
    json_data=json.dumps(data)
    headers={'content-type':'application/json'}
    r=requests.post(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
#post_data()

def put_data():
    data={
        "id":8,
        "name":"lonni",
        "dept":"MFA"
    }
    json_data=json.dumps(data)
    headers={"content-type":"application/json"}
    r=requests.put(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
#put_data()

def delete_data():
    data={"id":15}
    json_data=json.dumps(data)
    headers={"content-type":'application/json'}
    r=requests.delete(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
delete_data()