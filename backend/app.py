from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    # Accept JSON (from axios) OR form-encoded (if you ever send that)
    data = request.get_json(silent=True) or request.form
    name = (data.get("name") or "").strip()
    age = (data.get("age") or "").strip()

    if not name or not age:
        return jsonify({"message": "Please provide both name and age."}), 400

    return jsonify({"message": f"Hello {name}, you are {age} years old!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
