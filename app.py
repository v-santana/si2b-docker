import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def fibonacci():
    a = 1
    b = 1
    x = '1, '
    for i in range(49):
        b = b + a
        a = b - a
        x += str(a) + ', '
    return x


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
