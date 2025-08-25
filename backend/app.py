from flask import Flask, request, jsonify
from flask_cors import CORS

# 1. Initialize the Flask app once
app = Flask(__name__)

# 2. Apply CORS to the app instance
# This allows requests from any origin. For production, you might want to restrict this.
# Example: CORS(app, resources={r"/api/*": {"origins": "https://your-frontend-domain.com"}})
CORS(app)

# 3. Define the first route
@app.route("/api/hello")
def hello():
    """A simple endpoint to confirm the backend is running."""
    return jsonify({"message": "Hello from the backend!"})

# 4. Define the second route
@app.route('/process', methods=['POST'])
def process():
    """Processes incoming JSON data with a name and age."""
    # Get JSON data from the request. `silent=True` prevents an error if the body isn't JSON.
    data = request.get_json(silent=True)

    # Basic validation to ensure data is a dictionary
    if not isinstance(data, dict):
        return jsonify({"message": "Invalid JSON format. Please send an object."}), 400

    # Retrieve name and age, stripping any leading/trailing whitespace
    name = (data.get("name") or "").strip()
    age = str(data.get("age") or "").strip() # Convert age to string to be safe

    # Validate that both name and age were provided
    if not name or not age:
        return jsonify({"message": "Please provide both 'name' and 'age' in the JSON payload."}), 400

    # Return a success message
    return jsonify({"message": f"Hello {name}, you are {age} years old!"})

# 5. Run the app
if __name__ == "__main__":
    # host="0.0.0.0" makes the server accessible on your local network
    # debug=True enables auto-reloading on code changes and provides detailed error pages
    app.run(host="0.0.0.0", port=5000, debug=True)
