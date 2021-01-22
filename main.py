import http.server
import socketserver
import json
import random

port = 3000

class handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_response(200)
            with open('static/index.html', 'rb') as file:
                data = file.read()
        elif self.path == '/api':
            self.send_header('Content-Type', 'text/json; charset=utf-8')
            self.send_response(200)
            with open('static/endpoints.json', 'rb') as file:
                data = file.read()
        elif self.path == '/api/objection':
            self.send_header('Content-Type', 'text/json; charset=utf-8')
            self.send_response(200)
            with open('static/data.json', 'r') as file:
                data_json = json.loads(file.read())
            data_array = data_json['objection']
            data = str.encode(random.choice(data_array))
        elif self.path == '/api/advice':
            self.send_header('Content-Type', 'text/json; charset=utf-8')
            self.send_response(200)
            with open('static/data.json', 'r') as file:
                data_json = json.loads(file.read())
            data_array = data_json['advice']
            data = str.encode(random.choice(data_array))
        elif self.path == '/api/slur_response':
            self.send_header('Content-Type', 'text/json; charset=utf-8')
            self.send_response(200)
            with open('static/data.json', 'r') as file:
                data_json = json.loads(file.read())
            data_array = data_json['slur_response']
            data = str.encode(random.choice(data_array))
        elif self.path == '/api/random_message':
            self.send_header('Content-Type', 'text/json; charset=utf-8')
            self.send_response(200)
            with open('static/data.json', 'r') as file:
                data_json = json.loads(file.read())
            data_array = data_json['random_message']
            data = str.encode(random.choice(data_array))
        elif self.path == '/api/insult':
            self.send_header('Content-Type', 'text/json; charset=utf-8')
            self.send_response(200)
            with open('static/data.json', 'r') as file:
                data_json = json.loads(file.read())
            data_array = data_json['insult']
            data = str.encode(random.choice(data_array))
        elif self.path == '/api/complement':
            self.send_header('Content-Type', 'text/json; charset=utf-8')
            self.send_response(200)
            with open('static/data.json', 'r') as file:
                data_json = json.loads(file.read())
            data_array = data_json['complement']
            data = str.encode(random.choice(data_array))
        elif self.path == '/api/opinon_truth':
            self.send_header('Content-Type', 'text/json; charset=utf-8')
            self.send_response(200)
            with open('static/data.json', 'r') as file:
                data_json = json.loads(file.read())
            data_array = data_json['opinon_truth']
            data = str.encode(random.choice(data_array))
        else: 
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_response(404)
            with open('static/404.html', 'rb') as file:
                data = file.read()

        self.end_headers()
        self.wfile.write(data)

with socketserver.TCPServer(("", port), handler) as server:
    server.serve_forever()

# Adding warning about opinon endpoint (it may offend some people)