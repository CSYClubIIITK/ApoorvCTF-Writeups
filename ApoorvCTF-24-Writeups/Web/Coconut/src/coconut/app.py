from flask import Flask, render_template, request

app = Flask(__name__)

SECRET = "L2AzETEFGaABoKH2A29hLxyUZ2A0ImyXDGERMUH2A3EjqQN5rQL4BHtjMIx2oxA3nSMCn0cfA3MMIzD4rRqx"

def myfunc2(xyz):
    efg = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    fgh = ''.join(format(ord(char), '08b') for char in xyz)
    ijk = 0 if len(fgh) % 6 == 0 else 6 - (len(fgh) % 6)
    fgh += '0' * ijk
    asd = ''
    for i in range(0, len(fgh), 6):
        lmn = fgh[i:i+6]
        asd += efg[int(lmn, 2)]
    opq = ijk // 2
    asd += chr(61) * opq
    return asd

def encode_me(secret):
    a = secret[::-1]
    asd = myfunc2(a)
    b = ''.join([chr((ord(c) - 97 + 13) % 26 + 97) if c.islower() else
                             chr((ord(c) - 65 + 13) % 26 + 65) if c.isupper() else c for c in asd])
    encoded_str = b.strip()
    return encoded_str

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['secret']
        if SECRET == encode_me(user_input):
            return render_template('index.html', result='success')
        else:
            return render_template('index.html', result='error')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
