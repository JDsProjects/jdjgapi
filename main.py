from flask import Flask

app = Flask("JD-api")

@app.route("/")
def main():
  return "Welcome to the JDJG Inc. Official api :D"

app.run(host='0.0.0.0', port=3000,threaded=True)