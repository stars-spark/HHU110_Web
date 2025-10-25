from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许本地跨域调试

@app.get("/api/ping")
def ping():
    return jsonify({"msg": "pong"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
