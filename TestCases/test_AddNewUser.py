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

addUserSchema = {
    "type": "object",
    "properties": {
        "code": {"type": "integer"},
        "meta": {"type": "null"},
        "data": {"type": "object",
                 "properties": {
                     "id": {"type": "integer"},
                     "name": {"type": "string"},
                     "email": {"type": "string"},
                     "gender": {"type": "string"},
                     "status": {"type": "string"},
                     "created_at": {"type": "string"},
                     "updated_at": {"type": "string"}
                 }},
    },
}


def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=addUserSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

print("Create New User")
response = theApp().addUser(userData)
print("The response is: ")
print(response)
jsonData = json.loads(response.text)

def test_addNewUser_validate_satus_Code():
    print(response.status_code)
    assert response.status_code == 200
    filter = parse('$.code')
    match = [match.value for match in filter.find(jsonData)]
    print(match)
    if match[0] != 201:
        filter = parse('$.data[0]')
        reason = [match.value for match in filter.find(jsonData)]
        assert match[0] == 201, f"The reason for failure = {reason}"

    
def test_addNewUser_validate_schema():
    print("Validaating the JSON schema")
    isValid = validateJson(jsonData)
    if isValid:
        print("The response is: ")
        print("Given JSON data is Valid")
    else:
        print(jsonData)
        print("Given JSON data is InValid")
    assert isValid, f"The schema verification is not pass = {jsonData}"

