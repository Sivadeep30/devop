from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!!'

if __name__ == '__main__':
    # Binding to a specific host and port
    app.run(debug=True, host='0.0.0.0', port=5000)
