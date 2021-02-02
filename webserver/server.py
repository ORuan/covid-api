from http.server import BaseHTTPRequestHandler, HTTPServer


hostName = "localhost"
serverPort = 8081

class MyServer(BaseHTTPRequestHandler):
    
    print(f'[*] -- http://{hostName}:{serverPort}')

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()


webServer = HTTPServer((hostName, serverPort), MyServer)
