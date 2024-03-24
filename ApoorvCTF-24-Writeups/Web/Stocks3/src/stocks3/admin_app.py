from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def admin():
    return "apoorvctf{CONGRat5_yOU_ARE_s$Rf_ExpERt}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6002)
