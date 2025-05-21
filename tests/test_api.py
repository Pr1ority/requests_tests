import requests


def test_get_post_id(base_url):
    r = requests.get(f"{base_url}capsules/C112")
    assert r.status_code == 200, 'Ошибка запроса'
    assert 'capsule_id' in r.json(), 'Неверные поля'
    

def test_get_todos_id(base_url):
    r = requests.get(f"{base_url}dragons/dragon1")
    assert r.status_code == 200, 'Ошибка запроса'
    assert 'id' in r.json(), 'Отсутствуют необходимые поля'


def test_get_fake_id(base_url):
    r = requests.get(f"{base_url}dragons/dragon514")
    assert r.status_code == 404, 'Эндпоинт найден, хотя не должен'


def test_get_info(base_url):
    r = requests.get(f"{base_url}info")
    assert r.status_code == 200, 'Эндпоинт не найден'


def test_get_landpads(base_url):
    r = requests.get(f"{base_url}landpads")
    assert r.status_code == 200, "Эндпоинт не найден"