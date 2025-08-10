#Elevate Lab Internship
#Task4 : Build a REST API with Flask
#Date: 58 Aug 2025
#Objective : ICreate a REST API that manages user data.

#================================================================================
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage (acting as our database)
users = {}

#  GET - we will retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    """Return all users."""
    return jsonify(users)

#  GET - here we retrieve a single user by ID
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Return user details by ID."""
    user = users.get(user_id)
    if user:
        return jsonify({user_id: user})
    return jsonify({"error": "User not found"}), 404

# POST - Create a new user
@app.route('/users', methods=['POST'])
def add_user():
    """Add a new user."""
    data = request.get_json()
    user_id = str(data.get('id'))
    name = data.get('name')

    if not user_id or not name:
        return jsonify({"error": "ID and name are required"}), 400

    if user_id in users:
        return jsonify({"error": "User already exists"}), 400

    users[user_id] = {"name": name}
    return jsonify({"message": "User added successfully"}), 201

# PUT - Update an existing user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """Update user details."""
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({"error": "Name is required"}), 400

    users[user_id]['name'] = name
    return jsonify({"message": "User updated successfully"})

# DELETE - Remove a user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user."""
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted successfully"})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
