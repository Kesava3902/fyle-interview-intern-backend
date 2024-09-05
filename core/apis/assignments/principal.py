from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to simulate the response
response_data = {
    "data": [
        {
            "content": "ESSAY T1",
            "created_at": "2021-09-17T03:14:01.580126",
            "grade": None,
            "id": 1,
            "state": "SUBMITTED",
            "student_id": 1,
            "teacher_id": 1,
            "updated_at": "2021-09-17T03:14:01.584644"
        }
    ]
}

@app.route('/api/submit', methods=['GET'])
def get_essay_submission():
    # Extract the custom header X-Principal
    principal_header = request.headers.get('X-Principal')
    
    # Check if the header is present and valid
    if principal_header:
        # Simulate processing of the principal data
        # Here, we assume principal_header is a valid JSON string
        principal_data = request.headers.get('X-Principal')
        
        # Example log or validation (can be expanded with actual checks)
        print(f"Received X-Principal header: {principal_data}")
        
        # Return the JSON response
        return jsonify(response_data), 200
    else:
        return jsonify({"error": "X-Principal header is required"}), 400

if __name__ == '__main__':
    app.run(debug=True)