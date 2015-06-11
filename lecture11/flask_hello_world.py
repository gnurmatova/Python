from flask import Flask

#create a Flask application
#the argument to Flask is the name of the application's module
#since we are running our application in a single file, leave it as __name__
app=Flask(__name__)

#relative path to the root of your application
@app.route('/')
def hello_world():
    return 'Hello World!'

app.run()