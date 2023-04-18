from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/robots.txt")
def robots():
    return render_template("robots.txt")

@app.route("/thisisanotoriouslylongandrandomfilenamecontainingsecrets.html")
def secret():
    return render_template("thisisanotoriouslylongandrandomfilenamecontainingsecrets.html")

@app.route("/*")
def wildcard():
    return ""

@app.errorhandler(404)
def page_not_found(e):
    return ""

if __name__ == '__main__':
    app.run()