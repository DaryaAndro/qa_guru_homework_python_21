import json
import os

from jsonschema.validators import validate
from conftest import resources_path, api_requests


def test_get_list_users_schema():
    with open(os.path.join(resources_path, 'get_list_users_schema.json')) as file:
        schema = json.loads(file.read())

    response = api_requests(service='regres', method='get', url='/api/users')
    validate(response.json(), schema)


def test_get_single_user_schema():
    with open(os.path.join(resources_path, 'get_single_user_schema.json')) as file:
        schema = json.loads(file.read())

    response = api_requests(service='regres', method='get', url='/api/users/1')
    validate(response.json(), schema)
