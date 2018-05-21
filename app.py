from flask import Flask, request
import json
app = Flask(__name__)


@app.route('/write', methods=['POST'])
def write():
    post = request.get_json()
    phrase = post['phrase']
    with open("storage.txt", "a") as f:
        f.write(phrase + "\n")
    return "Posted to storage.txt: " + phrase


@app.route('/read')
def read():
    with open("storage.txt", "r") as f:
        phrase_list = f.readlines()
        phrase_list = [phrase.rstrip("\n") for phrase in phrase_list]
    return json.dumps({"phrases": phrase_list})


if __name__ == '__main__':
    app.run(port=8080, debug=True)

