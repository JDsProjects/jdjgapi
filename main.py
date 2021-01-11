import http.server
import socketserver
import json
import math

port = 3000

class handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        if self.path == '/':
            file = open('static/index.html','rb')
            data = file.read()
            file.close()
        elif self.path == '/api/objection':
            file = open('static/data.json','r')
            data_json = file.read()
            file.close()
            data_dict = json.loads(data_json)
            data_array = data_dict["objection"]
            data = data_array[Math.floor(Math.random()*items.length)]
        else:
            file = open('static/404.html','rb')
            data = file.read()
            file.close()

        self.wfile.write(data)

with socketserver.TCPServer(("", port), handler) as server:
    server.serve_forever()