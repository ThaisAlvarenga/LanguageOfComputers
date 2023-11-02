from flask import Flask
app = Flask(__name__)

# python decorator
@app.route('/')
def helloWorld():
    return "Hello World!"

if __name__ == "__main__":
    app.run()