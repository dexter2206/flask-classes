import requests


if __name__ == '__main__':
    response = requests.post('http://localhost:5000/form', data={'foo': 1})
    print(response.text)