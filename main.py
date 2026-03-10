import subprocess as sp
from flask import Flask, jsonify, request
from urllib.parse import urlsplit

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping_entry():
    content = request.args.get("url")
    netloc = urlsplit(content).netloc
    if not content:
        return jsonify({'error': 'no url provided'}), 400

    print(content)
    ret=sp.run(['ping', '-c', '1', '-w', '50', netloc], capture_output=True)
    return jsonify({'url': netloc, 'status': ret.returncode}) 

if __name__ == "__main__":
    app.run(host = "0.0.0.0")

