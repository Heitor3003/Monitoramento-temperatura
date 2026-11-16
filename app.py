from flask import Flask, jsonify, render_template
from serial import ler_dados


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dados")
def dados():
    
    temp, umid = ler_dados()

    return jsonify({
        "temperatura":temp,
        "umidade": umid
    })

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)