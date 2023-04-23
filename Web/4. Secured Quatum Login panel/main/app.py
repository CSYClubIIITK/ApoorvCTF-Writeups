import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']

	conn = sqlite3.connect('users.db')
	cursor = conn.cursor()
	q = 'SELECT * FROM users WHERE username="'+username+'" AND password="'+password+'";'
	cursor.execute(q)
	user = cursor.fetchone()
	conn.close()

	if user:
		if user[1] != "admin":
			return redirect(url_for('profile', username=user[1]))
		else:
			return 'apoorvctf{dOub1e_quo7es_5uCk}'
	else:
		return 'user not found/invalid password'

@app.route('/register.html')
def register_page():
	return render_template("register.html")

@app.route('/register', methods=['POST'])
def register():
	username = request.form['username']
	password = request.form['password']

	conn = sqlite3.connect('users.db')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM users WHERE username=?', (username,))
	user = cursor.fetchone()

	if user:
		return 'user already exists'
	else:	
		cursor.execute('INSERT INTO users(username, password) VALUES(?, ?)', (username, password))
		conn.commit()
		conn.close()
	return redirect(url_for('index'))

@app.route('/profile/<username>')
def profile(username):
	conn = sqlite3.connect('users.db')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM users WHERE username=?', (username,))
	user = cursor.fetchone()
	conn.close()

	if user:
		if user[1] != "admin":
			return f'Welcome, {username}!'
		else:
			return "haha nice try"
	else:
		return 'User not found'

if __name__ == '__main__':
    app.run()
