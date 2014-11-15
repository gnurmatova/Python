from flask import Flask

app=Flask(__name__)

@app.route('/input')
def input():
    return 'receive input here'

@app.route('/output')
def output():
    return 'display output here'

@app.route('/weather')
def weather():
    return ' snowing'

app.run()