from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Log the request path
        print("Path:", self.path)

        # Log the headers
        print("Headers:", self.headers)

        # Read and log the data sent in the POST request
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print("Received POST data:", post_data.decode('utf-8'))

        # Respond with 200 OK
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"SMS archived successfully!")

# Run the HTTP server
server_address = ('', 8080)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

print("Starting HTTP server on port 8080...")
httpd.serve_forever()
