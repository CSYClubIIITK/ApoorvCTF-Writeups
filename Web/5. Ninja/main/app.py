from flask import Flask, render_template,render_template_string, request

app = Flask(__name__)
app.secret_key = 'ApoorvCTF{you_ar3_a_rEA11y_go0D_nINj4}'

@app.route("/")
def index():
    name = None
    name = request.args.get("name")
    if name is not None:
        template = "<p>こんにちは "+name+"</p>"
        return render_template_string(template)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run()