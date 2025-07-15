#!/usr/bin/env python3

import http.server
import socketserver
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

def run_server():
    web_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(web_dir)
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()