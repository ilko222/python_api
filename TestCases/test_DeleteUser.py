import pytest
import requests
from the_app import theApp
import json
import jsonschema
from jsonschema import validate
from jsonpath_ng import jsonpath, parse

userData = {
    'name': 'Test User',
    'gender': 'Male',
    'email': 'test.email@email',
    'status': 'Active'
}

class DeleteUser:
    def getUserIdFromResponce(self, response):
        jsonData = json.loads(response.text)
        filter = parse('$.data[0].id')
        id = [match.value for match in filter.find(jsonData)]
        return id[0]

    def getUserID (self, userEmail):
        print("Get users ID")
        response = theApp().getUserByEmail(userEmail)
        print("The response is: ")
        print(response.text)
        return response


print("Get Email")
userEmail = userData.get("email")
print(userEmail)
idResponce = DeleteUser().getUserID(userEmail)
id = DeleteUser().getUserIdFromResponce(idResponce)
print("Delete the user")
print(id)
response = theApp().deleteUser(str(id))


def test_deleteUser_validate_satus_Code():
    print(response.status_code)
    assert response.status_code == 200
    filter = parse('$.code')
    jsonData = json.loads(response.text)
    match = [match.value for match in filter.find(jsonData)]
    print(match)
    if match[0] != 204:
        filter = parse('$.data[0]')
        filter = parse('$.id')
        reason = filter.find(jsonData)
        # reason = [match.value for match in filter.find(jsonData)]
        assert match[0] == 204, f"The reason for failure = {reason}"


