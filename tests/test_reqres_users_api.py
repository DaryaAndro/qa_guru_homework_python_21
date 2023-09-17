from conftest import api_requests


def test_get_single_user_not_found():
    response = api_requests(service='regres', method='get', url='/api/users/44')

    assert response.status_code == 404


def test_get_list_users_page():
    page = 1
    per_page = 6
    total = 12

    response = api_requests(service='regres', method='get', url='/api/users', params={"page": page})

    assert response.status_code == 200
    assert response.json()['page'] == 1
    assert response.json()['per_page'] == per_page
    assert len(response.json()['data']) == per_page
    assert response.json()['total'] == total


def test_first_user_on_page_2():
    page = 2

    response = api_requests(service='regres', method='get', url='/api/users', params={"page": page})

    assert response.json()['data'][0]['id'] == 7
    assert response.json()['data'][0]['email'] == 'michael.lawson@reqres.in'


def test_empty_data_page_3():
    page = 3

    response = api_requests(service='regres', method='get', url='/api/users', params={"page": page})

    assert response.json()['page'] == 3
    assert response.json()['total_pages'] == 2
    assert len(response.json()['data']) == 0


def test_post_create_user():
    name = 'Dasha'
    job = 'QA'

    response = api_requests(service='regres', method='post', url='/api/users',
                            json={"name": name, "job": job})

    assert response.status_code == 201
    assert response.json()['name'] == name
    assert response.json()['job'] == job


def test_put_update_user():
    name = 'Dasha'
    job = 'QA manual'

    response = api_requests(service='regres', method='put', url='/api/users/2',
                            json={"name": name, "job": job})

    assert response.status_code == 200
    assert response.json()['name'] == name
    assert response.json()['job'] == job


def test_delete_user():
    response = api_requests(service='regres', method='delete', url='/api/users/2')

    assert response.status_code == 204


def test_post_register_successful():
    email = 'eve.holt@reqres.in'
    password = 'pistol'

    response = api_requests(service='regres', method='post', url='/api/register',
                            json={"email": email, "password": password})

    assert response.status_code == 200
    assert response.json()['token'] is not None


def test_post_register_unsuccessful():
    email = 'sydney@fife'

    response = api_requests(service='regres', method='post', url='/api/register',
                            json={"email": email, "password": ''})

    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'
