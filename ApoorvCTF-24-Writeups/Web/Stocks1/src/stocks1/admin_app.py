from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def admin():
    return "apoorvctf{st0Nk$_go_8RrR}"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)
