from flask import Flask
app=Flask(__name__)

def hello_world():
    return '<p>Hello world!</p>'

if __name__ == "__main__":
    app.run(port=5000,debug=True)