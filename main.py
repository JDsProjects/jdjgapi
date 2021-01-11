import http.server
import socketserver
import json
import random

port = 3000

class handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        if self.path == '/':
            with open('static/index.html', 'rb') as file:
                data = file.read()
        elif self.path == '/api':
            with open('static/endpoints.json', 'rb') as file:
                data = file.read()
        elif self.path == '/api/objection':
            with open('static/data.json', 'r') as file:
                data_json = json.loads(file.reaohd())
            data_array = data_json["objection"]
            data = str.encode(random.choice(data_array))
        elif self.path == '/api/advice':
            with open('static/data.json', 'r') as file:
                data_json = json.loads(file.read())
            data_array = data_json["advice"]
            data = str.encode(random.choice(data_array))
        else: 
            with open('static/404.html', 'rb') as file:
                data = file.read()

        self.wfile.write(data)

with socketserver.TCPServer(("", port), handler) as server:
    server.serve_forever()