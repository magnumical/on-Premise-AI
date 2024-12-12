from flask import Flask, request, jsonify
import subprocess
import time
from threading import Lock

app = Flask(__name__)

# Mutex for managing shared resources (e.g., GPU)
resource_lock = Lock()

@app.route('/process', methods=['POST'])
def process():
    try:
        # Log the request
        print("Request received:", request.json)

        # Acquire lock for resource
        resource_lock.acquire()

        # Sequential execution: Container 1
        result1 = subprocess.run(
            ["docker", "exec", "container1", "python", "code1.py"],
            capture_output=True, text=True
        )
        if result1.returncode != 0:
            return jsonify({"status": "error", "message": result1.stderr}), 500

        # Sequential execution: Container 2
        result2 = subprocess.run(
            ["docker", "exec", "container2", "python", "code2.py"],
            capture_output=True, text=True
        )
        if result2.returncode != 0:
            return jsonify({"status": "error", "message": result2.stderr}), 500

        # Release the lock
        resource_lock.release()

        # Prepare the combined response
        response = {
            "status": "success",
            "code1_output": result1.stdout.strip(),
            "code2_output": result2.stdout.strip(),
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
        }
        return jsonify(response)

    except Exception as e:
        # Release the lock in case of failure
        if resource_lock.locked():
            resource_lock.release()
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
