import requests

server_url = "http://XX.XX.XX.XX:5000/process"

data = {
    "message": "Hello from Client"
}

try:
    response = requests.post(server_url, json=data)
    if response.status_code == 200:
        print("Response from server:", response.json())
    else:
        print("Failed to get a valid response. Status code:", response.status_code)
except Exception as e:
    print("Error connecting to server:", str(e))
