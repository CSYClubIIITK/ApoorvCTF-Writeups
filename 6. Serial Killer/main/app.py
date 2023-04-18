import pickle
from uuid import uuid1
from flask import Flask, make_response, request, render_template, redirect, url_for
from base64 import b64encode, b64decode

app = Flask(__name__)

# dummy items
all_items = []
for i in range(12):
    item = {
        'id': i,
        'name': f'item {i}',
        'price': f'Rs. {i}'
    }
    all_items.append(item)

@app.route('/', methods=['GET'])
def index():
    cart = request.cookies.get('cart')
    if cart == None:
        response = make_response(render_template("index.html", all_items=all_items))
        cart = []
        response.set_cookie('cart', b64encode(pickle.dumps(cart)))
        return response
    else:
        return render_template("index.html", all_items=all_items)

@app.route("/add", methods=["POST"])
def add():
    cart = request.cookies.get('cart')
    if cart is not None:
        cart = pickle.loads(b64decode(cart))
        item_id = request.form['item']
        cart.append(all_items[int(item_id)])
        response = make_response("Item added successfully")
        response.set_cookie('cart', b64encode(pickle.dumps(cart)))
        return response

    return redirect(url_for('index'))

@app.route("/view")
def view():
    cart = request.cookies.get('cart')
    if cart is not None:
        cart = pickle.loads(b64decode(cart))
        for i in range(len(cart)):
            cart[i] = cart[i]
        return render_template("cart.html", all_items=cart)
    else:
        return redirect(url_for("index"))

@app.route("/clear")
def clear():
    response = make_response("cart cleared successfully")
    cart = []
    response.set_cookie('cart', b64encode(pickle.dumps(cart)))
    return response

if __name__ == "__main__":
    app.run()