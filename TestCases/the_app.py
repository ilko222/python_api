import requests

api_base_url = 'https://gorest.co.in'
endpoint_path = '/public-api/users'
token = '01352ff6e24d83cc53e1d81724aec93fdedd3021dd0f313e6f6295e79bd66d5b'
headers = {
    'Accept':'application/json',
    'Content-Type':'application/json',
    'Authorization':f'Bearer {token}'
}
userId = '1343'
userData = {
    'name':'Test User',
    'gender':'Male',
    'email':'test.email@email',
    'status':'Active'
    }
updatePayload = {
    'name':'Test User2'
}
endpoint = f"{api_base_url}{endpoint_path}"


class theApp:
    def getUsers(self):
        try:
            r = requests.get(endpoint)
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def addUser(self, payload):
        try:
            r = requests.post(endpoint, json=payload, headers=headers)
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def getUserByEmail(self, email):
        try:
            r = requests.get(endpoint+'?email='+email, headers=headers)
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def deleteUser(self, userToDelete):
        try:
            r = requests.delete(endpoint+'/'+userToDelete, headers=headers)
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def upadeteUser (self, userId, payload):
        try:
            r = requests.patch(endpoint+'/'+userId, json=payload, headers=headers)
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    # getUsers = requests.get(endpoint)
    # addUser = requests.post(endpoint, json=userData, headers=headers)
    # deleteUser = requests.delete(endpoint+'/'+userId, headers=headers)
    # print(getUsers.status_code)
    # print(getUsers.text)
    # print("------------------------------------------------/n ------------------------------------")
if __name__ == '__main__':
    response = theApp().deleteUser(1464)
    print(response.status_code)
    print(response.text)
    # print("------------------------------------------------/n ------------------------------------")
    # response = upadeteUser(userId,updatePayload)
    # print(response.status_code)
    # print(response.text)