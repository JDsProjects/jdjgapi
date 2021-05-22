from flask import Flask
import json, random

app = Flask(__name__)

@app.route('/')
def handleRoot():
    with open('index.html', 'r') as file:
        data = file.read(), 200, {'content-type':'text/html'}
    return data

@app.route('/api/')
def handleApi():
    with open('api.html', 'r') as file:
        data = file.read(), 200, {'content-type':'text/html'}
    return data


@app.route('/api/<endpoint>')
def handleEndpoint(endpoint):
  with open('data.json', 'r') as file:
    dataJson = json.loads(file.read())
  try:
      dataArray = dataJson[endpoint]
      tempData = str(random.choice(dataArray))
      if endpoint == "objection" or endpoint == "opinional":
        tempDict = {"url": tempData}
      else:
        tempDict = {"text": tempData}
      data = json.dumps(tempDict), 200, {'content-type':'application/json'}
        
  except KeyError as e:
    print(e)
    errorDict={"error":f"{endpoint} isn't a valid endpoint"}
    data = json.dumps(errorDict), 404, {'content-type':'application/json'}
  return data

# hi
@app.errorhandler(404)
def handle404(error):
    with open('404.html', 'r') as file:
        data = file.read()
    return data, 404, {'content-type':'text/html'}

app.run(host='0.0.0.0', port=3000)