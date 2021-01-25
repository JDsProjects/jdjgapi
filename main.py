from flask import Flask
import json
import random

app = Flask(__name__)

@app.route('/')
def handleRoot():
    with open('index.html', 'r') as file:
        data = file.read()
    return data

@app.route('/api/<endpoint>')
def handleEndpoint(endpoint):
  if endpoint == "":
    with open('api.html', 'r') as file:
        data = file.read()
  else:
    with open('data.json', 'r') as file:
        data_json = json.loads(file.read())
    try:
        data_array = data_json[endpoint]
    except KeyError as e:
        print(e)
    data = str.encode(random.choice(data_array))
  return data

@app.errorhandler(404)
def handle404(error):
    with open('404.html', 'r') as file:
        data = file.read()
    return data

app.run(host='0.0.0.0', port=3000)