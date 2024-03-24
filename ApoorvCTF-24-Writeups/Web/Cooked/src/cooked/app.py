from flask import Flask, render_template, request, redirect, make_response
import base64
import json

app = Flask(__name__)

passwords = {'test': 'test', 'admin':'qwertyuiopreallyhardunguessablepasswordthatyoucantguessbecauseitstoolong'}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in passwords.keys() and password == passwords[username]:
        # Encode user information to base64 and create a cookie
        user_data = {'user': username}
        encoded_data = base64.b64encode(json.dumps(user_data).encode()).decode()
        response = make_response(redirect('/dashboard'))
        response.set_cookie('user_data', encoded_data)
        return response
    else:
        return redirect('/')

@app.route('/dashboard')
def dashboard():
    # Retrieve user information from the cookie and decode it
    encoded_data = request.cookies.get('user_data', '')
    if encoded_data:
        user_data = json.loads(base64.b64decode(encoded_data).decode())
        username = user_data.get('user', '')
        if username != 'admin':
            return f'Welcome to the dashboard, {username}!'
        else:
            return f'Welcome to the dashboard, {username}!<br /> apoorvctf{{7IM3_TO_CoOk_F149$!}}'
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
