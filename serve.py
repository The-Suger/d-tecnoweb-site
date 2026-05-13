import http.server
import os

os.chdir("/Users/satokanta/Desktop/claude code work用/d-tecnoweb")

handler = http.server.SimpleHTTPRequestHandler
with http.server.HTTPServer(("", 3456), handler) as httpd:
    httpd.serve_forever()
