import requests

def reqip():
    response = requests.get('https://httpbin.org/ip')
    return('Your IP is {0}'.format(response.json()['origin']))

def hello():
    print ('Hello World from function')

if __name__ == "__main__":
    hello()