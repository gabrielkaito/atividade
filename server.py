from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello World")

if __name__ == "__main__":
    port = 3000
    server_address = ("", port)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Server running on http://localhost:{port}")
    httpd.serve_forever()
