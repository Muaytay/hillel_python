# Импортируем библиотеку http запросов
import requests
from requests.exceptions import HTTPError

# Аппробирование метода get
try:
    url = 'https://reqres.in/api/users?page=2'
    response = requests.get(url)
    response.raise_for_status()
except HTTPError as http_error:
    print(f'GET: возникла HTTP ошибка: {http_error}')
except Exception as error:
    print(f'GET: возникла другая ошибка: {error}')
else:
    print('-'*20)
    print('GET запрос успешно обработан:')
    print(response.json())
    print('-' * 20)
    print()


# Аппробирование метода post
try:
    url = 'https://reqres.in/api/users'
    data = {
        "name": "morpheus",
        "job": "leader"
    }

    response = requests.post(url, data=data)
    response.raise_for_status()
except HTTPError as http_error:
    print(f'POST: возникла HTTP ошибка: {http_error}')
except Exception as error:
    print(f'POST: возникла другая ошибка: {error}')
else:
    print('-'*20)
    print('POST запрос успешно обработан:')
    print(response.json())
    print('-' * 20)
    print()


# Аппробирование метода put
try:
    url = 'https://reqres.in/api/users/2'
    data = {
        "name": "morpheus",
        "job": "leader"
    }

    response = requests.put(url, data=data)
    response.raise_for_status()
except HTTPError as http_error:
    print(f'PUT: возникла HTTP ошибка: {http_error}')
except Exception as error:
    print(f'PUT: возникла другая ошибка: {error}')
else:
    print('-'*20)
    print('PUT запрос успешно обработан:')
    print(response.json())
    print('-' * 20)
    print()

# Аппробирование метода patch
try:
    url = 'https://reqres.in/api/users/2'
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = requests.patch(url, data=data)
    response.raise_for_status()
except HTTPError as http_error:
    print(f'PATCH: возникла HTTP ошибка: {http_error}')
except Exception as error:
    print(f'PATCH: возникла другая ошибка: {error}')
else:
    print('-'*20)
    print('PATCH запрос успешно обработан:')
    print(response.json())
    print('-' * 20)
    print()


# Аппробирование метода delete
try:
    url = 'https://reqres.in/api/users/2'
    response = requests.delete(url)
    response.raise_for_status()
except HTTPError as http_error:
    print(f'DELETE: возникла HTTP ошибка: {http_error}')
except Exception as error:
    print(f'DELETE: возникла другая ошибка: {error}')
else:
    print('-'*20)
    print('DELETE запрос успешно обработан:')
    print(response)
    print('-' * 20)
    print()
