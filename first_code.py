from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    # Use '0.0.0.0' to bind to all available interfaces (including WiFi)
    app.run(host='0.0.0.0', port=5000)
