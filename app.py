from flask import Flask, request
import json
import os

port = 8080
storage_path = "storage.txt"

# if storage file does not exist, create one
if not os.path.exists(storage_path):
    open(storage_path, 'a').close()

app = Flask(__name__)


@app.route('/write', methods=['POST'])
def write():
    post = request.get_json()
    phrase = post['phrase']
    with open(storage_path, "a") as f:
        f.write(phrase + "\n")
    return "Posted to {}: {}".format(storage_path, phrase)


@app.route('/read')
def read():
    with open(storage_path, "r") as f:
        phrase_list = f.readlines()
        phrase_list = [phrase.rstrip("\n") for phrase in phrase_list]
    return json.dumps({"phrases": phrase_list})


if __name__ == '__main__':
    app.run(port=port, debug=True)

