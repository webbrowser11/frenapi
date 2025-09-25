from flask import Flask, request, jsonify, send_file
import os
wburl = os.getenv("WEBHOOK")
app = Flask(__name__)
@app.route("/api", methods=["POST"])
def message():
    data = request.get_json()
    message = data.get("message")
    __import__("requests").post(wburl, json={"content": message})
@app.route("/")
def index():
    return send_file("index.html")
if __name__ == "__main__":
    app.run(debug=True)

