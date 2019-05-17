import requests


if __name__ == '__main__':
    response = requests.post('http://localhost:5000/data', data='some test data')
    print(response.text)