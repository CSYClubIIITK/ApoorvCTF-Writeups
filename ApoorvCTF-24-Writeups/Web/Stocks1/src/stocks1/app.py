from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

stocks = [
    {"name": "HILTON", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vel justo eget justo eleifend faucibus.", "price": "100"},
    {"name": "HDFCBANK", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vel justo eget justo eleifend faucibus.", "price": "103"},
    {"name": "ABINFRA", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vel justo eget justo eleifend faucibus.", "price": "107"},
    {"name": "HAVELLS", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vel justo eget justo eleifend faucibus.", "price": "99"},
    {"name": "IDFC", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vel justo eget justo eleifend faucibus.", "price": "115"},
    {"name": "ITC", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vel justo eget justo eleifend faucibus.", "price": "120"},
]

@app.route('/')
def index():
    return render_template('index.html', stocks=stocks)

@app.route('/stock/<int:stock_id>')
def stock(stock_id):
    if 0 <= stock_id < len(stocks):
        return render_template('stock.html', stock=stocks[stock_id], stock_id=stock_id)
    else:
        return "Stock not found"

@app.route('/get_price')
def get_price():
    url = request.args.get('url')
    try:
        response = requests.get(url)
        response.raise_for_status()

        return response.content

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
