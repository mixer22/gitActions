from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify({"message": "Hello, Flask"})

def get_quote_of_the_day():
    return "The only limit is your mind."

@app.route("/quote")
def quote():
    quote_text = get_quote_of_the_day()
    return jsonify({"quote": quote_text})
