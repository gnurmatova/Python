
from flask import Flask, send_file, request, abort, make_response
from PIL import Image
from PIL import ImageFilter

app=Flask(__name__)

@app.route('/processimage', methods=['POST'])
def processimage():
	f = request.files['file']
	im = Image.open(f)
	im = im.filter(ImageFilter.BLUR)
	im.save("images/site.png")
	return send_file("images/site.png", mimetype='image/png')
	
app.run(debug = True)