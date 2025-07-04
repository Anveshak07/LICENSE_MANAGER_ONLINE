import requests

url = "http://127.0.0.1:5000/validate"
data = {
    "license_key": "8E26F2942E6B4B08",  # ✅ updated key
    "machine_id": "MACHINE_002"         # ✅ must match
}

response = requests.post(url, json=data)
print(response.json())
