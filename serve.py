from http.server import BaseHTTPRequestHandler, HTTPServer

class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200) # make sure that is an okay env
        self.send_header("Content-type", "text/html") # make sure that it is not GIF 😂
        self.end_headers();

        self.wfile.write(b"<!DOCTYPE html>")
        self.wfile.write(b"<html lang = 'en>")
        self.wfile.write(b"<head>")
        self.wfile.write(b"<title>hello, title</title>")
        self.wfile.write(b"</head>")
        self.wfile.write(b"<body>")
        self.wfile.write(b"hello, world")
        self.wfile.write(b"</body>")
        self.wfile.write(b"</html>")

port = 8080 # specify the port number to be listened on
server_address = ("0.0.0.0", port) # specify the IP address that that you want to run your web server on 
httpd = HTTPServer(server_address, HTTPServer_RequestHandler)

httpd.serve_forever()

