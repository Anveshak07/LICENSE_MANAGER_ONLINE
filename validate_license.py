import requests

url = "http://127.0.0.1:5000/validate"

# Ask user for license key and machine ID
license_key = input("Enter license key: ").strip()
machine_id = input("Enter machine ID: ").strip()

if not license_key or not machine_id:
    print("❌ License key or machine ID is missing.")
else:
    data = {
        "license_key": license_key,
        "machine_id": machine_id
    }

    try:
        response = requests.post(url, json=data)
        result = response.json()
        print("✅ Server response:", result)
    except requests.exceptions.RequestException as e:
        print("❌ Error while contacting server:", e)
