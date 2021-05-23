from flask import Flask

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return "Hello Flask!"

@app.route("/contact")
def potato():
    return "Contact"

app.run(host="0.0.0.0")