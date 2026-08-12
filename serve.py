import http.server
import os
from pathlib import Path

os.chdir(Path(__file__).resolve().parent)

handler = http.server.SimpleHTTPRequestHandler
with http.server.HTTPServer(("", 3456), handler) as httpd:
    httpd.serve_forever()
