from flask import Flask, jsonify

app = Flask(__name__)

# Simulated user data (replace this with your actual data source)
users = {
    1: {"id": 1, "name": "John Doe", "email": "john@example.com"},
    2: {"id": 2, "name": "Jane Smith", "email": "jane@example.com"},
}

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


""" To test the microservice, uou can use a tool like cURL or Postman to test your microservice by sending HTTP requests to it.
For example, to get the details of user with ID 1, use the following cURL command:

curl http://localhost:5000/user/1

This will return a JSON response with the user details. """