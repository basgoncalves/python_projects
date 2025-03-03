from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Ensure the templates directory exists
TEMPLATES_DIR = os.path.join(app.root_path, 'templates')
if not os.path.exists(TEMPLATES_DIR):
    os.makedirs(TEMPLATES_DIR)

DATA_FILE = os.path.join(TEMPLATES_DIR, "users.json")

def load_users():
    """Loads users from the JSON file or returns an empty list."""
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                try:
                    data = json.load(f)
                    if isinstance(data, list):
                        return data
                    else:
                        print("Warning: JSON data is not a list. Returning empty list.")
                        return []
                except json.JSONDecodeError:
                    print("Warning: JSON decode error. Returning empty list.")
                    return []
        else:
            print("Info: users.json not found. Returning empty list.")
            return []
    except Exception as e:
        print(f"Error loading users: {e}. Returning empty list.")
        return []

def save_users(users):
    """Saves the users to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        if username:
            users = load_users()
            print(f"Users loaded: {users}") # Debug print
            if users is None:
                print("Error: load_users returned None") #Extra debug print.
                return render_template("index.html", error="Error loading users.")

            users.append({"username": username})
            save_users(users)
            return render_template("success.html", username=username)
        else:
            return render_template("index.html", error="Please enter a username.")

    return render_template("index.html")

@app.route("/users")
def get_users():
    """Returns all users as JSON."""
    users = load_users()
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)