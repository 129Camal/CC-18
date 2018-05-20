import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("localhost", 80), Handler)

httpd.serve_forever()