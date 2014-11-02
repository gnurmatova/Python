from wsgiref.simple_server import make_server
import re

def hello_world_app(environ, start_response):
	#print("ENVIRON:", environ)
	message=""
	status = '200 OK'
	headers = [('Content-type', 'html; charset=utf-8')]
	start_response(status, headers)
	if(len(environ['QUERY_STRING'])>1):
		message += "<br> Your data has been recieved:"
		for param in environ['QUERY_STRING'].split("&"):
			message += "<br>"+param
	message += "<h1>Welcome to the Zoo</h1>"
	message += "<form><br>Animal:<input type=text name='animal'>"
	message += "<br><br>Count:<input type=text name='count'>"
	message += "<br><br><input type='submit' name='Submit' ></form>"
	return[bytes(message,'utf-8')]

httpd = make_server('', 8000, hello_world_app)
print("Serving on port 8000...")


httpd.serve_forever()