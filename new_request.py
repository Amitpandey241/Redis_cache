import requests
import json

url = "http://192.168.128.3:5000/get_data"

payload = json.dumps({
    "code":"A302.TXT"
})
headers = {
    'Content-Type':'application/json'
}
param ={
    'C':'M',
    'O':'A'
}

response = requests.request("POST", url,headers= headers,params=param, data=payload)
print(response.text)