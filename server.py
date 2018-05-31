from flask import Flask
import requests

app=Flask(__name__)

@app.route("/")
def index():
    #headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    #r = requests.get('http://api.data.mos.ru/v1/datasets/2009/rows', headers=headers)
    session = requests.Session()
    response = session.get('http://api.data.mos.ru/v1/datasets/2009/rows', headers={'User-Agent': 'Mozilla/5.0'})

    print(response)
    print(response.headers)
    return "hi"

if __name__ == '__main__':
    app.run()