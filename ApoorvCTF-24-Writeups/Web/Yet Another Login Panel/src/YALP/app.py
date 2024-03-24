from flask import Flask,render_template,request,redirect,url_for,make_response,jsonify
import jwt
from cryptography.hazmat.primitives import serialization
import base64
import json

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == "test" and password == "test":
        payload = {'username': username}
        with open('private_key.pem', 'rb') as f:
            private_key = serialization.load_pem_private_key(f.read(), password=None)
        algorithm = 'RS256'
        token = bytes(jwt.encode(payload, private_key, algorithm=algorithm),'utf-8')
        resp = make_response(redirect(url_for('dashboard',username=username)))
        resp.set_cookie('token', token.decode('UTF-8'))
        return resp
    else:
         return "Please try again !!!"

@app.route("/dashboard/<username>",methods=['GET'])
def dashboard(username):
    token = request.cookies.get('token')
    if token is None:
        return "Missing authentication"

    header, payload, signature = token.split('.')
    decoded_header = base64.urlsafe_b64decode(header + '=' * (4 - len(header) % 4))
    decoded_header_str = decoded_header.decode('utf-8')
    header_json = json.loads(decoded_header_str)
    algorithm_type = header_json['alg']
    if username not in ['test', 'admin']:
        return jsonify({'status': 'error', 'message': 'invalid user'})
    verified = False

    if algorithm_type == "RS256":
        with open('public_key.pem', 'rb') as f:
            public_key = serialization.load_pem_public_key(f.read())
        decoded_jwt = jwt.decode(token,public_key, algorithms=['RS256'])
        payload_data = decoded_jwt['username']
        if username == payload_data:
            verified = True
        else:
            return jsonify({'status': 'error', 'message': 'The payload data and decrypted part of the JWT are different'})

    elif algorithm_type == "HS256":

        with open('secret_key.txt', 'r') as f:
            secret_key = f.read().strip()
        decoded_jwt = jwt.decode(token, secret_key, algorithms=['HS256'])
        payload_data = decoded_jwt['username']

        if username == payload_data:
            verified = True
        else:
            return jsonify({'status': 'error', 'message': 'The payload data and decrypted part of the JWT are different'})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid algorithm'})

    if verified:
        if username != "admin":
            return "welcome {}".format(username)
        elif username == "admin":
            return "ApoorvCTF{5eCr3t5_AreNT_SECrEt_ANYMore}"

@app.route('/')
def index():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
