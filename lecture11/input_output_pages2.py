
from flask import Flask, jsonify

app=Flask(__name__)

data=[{'fname':'Steve', 'lname':'Jobbs'},{'fname':'Bill', 'lname':'Gates'}]

@app.route('/input')
def input():
	return 'input here'

@app.route('/data', methods=['GET'])
def get_data():
	return jsonify({'data' : data})

app.run(debug = True)