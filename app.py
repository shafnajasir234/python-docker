from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Hello from Dockerized Python App 🚀",
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname())
    }

@app.route("/health")
def health():
    return jsonify({"status": "OK"})

@app.route("/env")
def env():
    return dict(os.environ)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
