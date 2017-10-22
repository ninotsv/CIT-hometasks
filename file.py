import requests;
response = requests.get("https://cit-home1.herokuapp.com/api/help")

print(response.content.decode('utf-8'))

def SignUp():
    response = requests.post("https://cit-home1.herokuapp.com/api/register",
     json={'Content-Type': 'application/json'})
    print(response.json())
    response = requests.get("https://cit-home1.herokuapp.com/api/check_me")
    print(response.json())

SignUp()

response=requests.get("https://cit-home1.herokuapp.com/api/headers")
