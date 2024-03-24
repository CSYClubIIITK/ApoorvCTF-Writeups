from flask import Flask
import random

app = Flask(__name__)

@app.route('/<int:stock_id>')
def send_price(stock_id):
    return {'price' : random.randint(100, 120)}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
