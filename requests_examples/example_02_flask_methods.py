import requests

PATHS = ['/get', '/post', '/both']

if __name__ == '__main__':
    for path in PATHS:
        url = f'http://localhost:5000{path}'

        print(f'Testing url {url} with GET method')

        response = requests.get(url)

        if response.ok:
            print(f'SUCCESS, response: {response.text}')
        else:
            print(f'FAILURE, status code: {response.status_code}')

        print(f'Testing url {url} with POST method')

        response = requests.post(url)

        if response.ok:
            print(f'SUCCESS, response: {response.text}')
        else:
            print(f'FAILURE, status code: {response.status_code}')