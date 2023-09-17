from conftest import api_requests


def test_get_breeds():
    limit = 10
    breed = 'Abyssinian'

    response = api_requests(service='catfact', method='get', url='/breeds', params={"limit": limit})

    assert response.status_code == 200
    assert response.json()['per_page'] == str(limit)
    assert len(response.json()['data']) == limit
    assert response.json()['data'][0]['breed'] == breed


def test_get_fact():
    len_max = 50
    response = api_requests(service='catfact', method='get', url='/fact', params={"max_length": len_max})

    assert response.status_code == 200
    assert response.json()['fact'] is not None
    assert response.json()['length'] <= len_max


def test_get_facts():
    default_limit = 10

    response = api_requests(service='catfact', method='get', url='/facts')

    assert response.status_code == 200
    assert response.json()['per_page'] == default_limit
    assert len(response.json()['data']) is not None
