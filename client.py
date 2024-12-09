
import requests

# Replace with the IP address of Server Computer (get it via ipconfig)
server_url = "http://172.21.37.140:5000/process"


data = {
    "message": "Hello from Computer 1"
}

try:
    # Send the POST request
    response = requests.post(server_url, json=data)

    # Print the server's response
    if response.status_code == 200:
        print("Response from server:", response.json())
    else:
        print("Failed to get a valid response. Status code:", response.status_code)
except Exception as e:
    print("Error connecting to server:", str(e))
