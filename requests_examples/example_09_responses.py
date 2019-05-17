import requests

PATHS = ['/tuple', '/triple', '/respobj', '/respobj2']

if __name__ == '__main__':
    for path in PATHS:
        print(30 * '=')
        print(f'Path: {path}')
        resp = requests.get(f'http://localhost:5000{path}')
        print(f'Text: {resp.text}')
        print(f'Headers: {resp.headers}')
        print(f'Status: {resp.status_code}')