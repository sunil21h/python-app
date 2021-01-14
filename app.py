from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "This is my first application!"

if __name__ == '__main__':
    app.run()
