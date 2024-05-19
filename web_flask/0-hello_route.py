from flask import Flask
''' web application that displays "Hello HBNB!"''' 
app = Flask(__name__)

@app.route('/airbnb-onepage/', methods=['GET'])
def hello_hbnb():
    return "Hello HBNB!"
