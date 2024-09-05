from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample response data
response_data = {
    "data": [
        {
            "created_at": "2024-01-08T07:58:53.131970",
            "id": 1,
            "updated_at": "2024-01-08T07:58:53.131972",
            "user_id": 3
        }
    ]
}

@app.route('/api/data', methods=['GET'])
def get_data():
    # Extract the custom header X-Principal
    principal_header = request.headers.get('X-Principal')
    
    # Check if the header is present and valid
    if principal_header:
        # Simulate processing the principal data (you can add validation here)
        print(f"Received X-Principal header: {principal_header}")
        
        # Return the JSON response
        return jsonify(response_data), 200
    else:
        return jsonify({"error": "X-Principal header is required"}), 400

if __name__ == '__main__':
    app.run(debug=True)