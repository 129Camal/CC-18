import http.server
import socketserver

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('localhost', 8001), Handler) as httpd:
    httpd.serve_forever()
