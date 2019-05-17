import requests

if __name__ == '__main__':
    response = requests.get('http://localhost:5000')
    print(response.text)