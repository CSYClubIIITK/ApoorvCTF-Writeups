from flask import Flask

app = Flask(__name__)

@app.route('/')
def admin():
    return "apoorvctf{Dn$_1snt_dNSinG}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
