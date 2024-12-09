from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    # Log the request (optional)
    print("Request received:", request.json)
    
    # Prepare the response
    response = {
        "status": "success",
        "timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return jsonify(response)

if __name__ == '__main__':
    # Replace with the specific IP of Server Computer
    app.run(host='XX.XX.XX.XX', port=5000)
