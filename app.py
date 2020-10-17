import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def fibonacci():
    a = 1
    b = 0
    cont = '0,'
    for i in range(51):
        x = a
        a = a + b
        b = x
        cont += str(a) + ","
    return cont


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
