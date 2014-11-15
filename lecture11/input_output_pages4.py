
from flask import Flask, jsonify, request, abort

app=Flask(__name__)

data=[{'fname':'Steve', 'lname':'Jobbs'},{'fname':'Bill', 'lname':'Gates'}]

@app.route('/createperson', methods=['POST'])
def create_person():
	print(request.json)
	if not request.json or not 'person' in request.json:
		abort(400)
	data.append(request.json['person'])
	return jsonify({'data' : data}), 201

@app.route('/data', methods=['GET'])
def get_data():
	return jsonify({'data' : data})

@app.route('/data/<int:id>', methods=['GET'])
def get_data_byid(id):
	return jsonify({'data' : data[id]})

@app.route('/search', methods=['GET'])
def search_data():
	query = request.args.get('query', '')
	for item in data:
		if item['fname'] == query or item['lname'] == query:
			return jsonify({'data' : [item]})
	return jsonify({})
app.run(debug = True)