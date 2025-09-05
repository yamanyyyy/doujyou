from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/test')
def index02():
    return 'Hello Test'

if __name__ == "__main__":
    app.run(debug=True)