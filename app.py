from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/')
def assignment_1():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    print(a)
    print(b)
    r = requests.post('https://jerdel-law-rest.herokuapp.com/', headers={'Content-Type': 'application/json'},
                      json={'a': a, 'b': b})
    data = r.json()
    print(data)
    return '<html>Hasil: %s</html>' % data['hasil']


if __name__ == '__main__':
    app.run()
