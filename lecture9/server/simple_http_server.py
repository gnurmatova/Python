from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.request import urlopen

class MyHTTPHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.end_headers()
		with self.wfile as f:
			try:
				java_app = urlopen("http://localhost:5100/rest/books")
				if(java_app.getcode() == 200):
					f.write(b"Port 5100: Status: SUCCESS")
				else:
					f.write(b"Port 5100: Status: FAIL")
			except:
				f.write(b"Port 5100: Status: FAIL")
		return

server = HTTPServer(("", 8000), MyHTTPHandler)
server.serve_forever()