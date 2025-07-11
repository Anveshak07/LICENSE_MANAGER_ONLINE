﻿# LICENSE_MANAGER_ONLINE
🛡️ License Manager - Online License Validation System
A professional, Flask-based license manager with client-server architecture that provides secure license key generation, validation, and expiration handling. Built for preventing unauthorized use of desktop software.

🚀 Features Implemented So Far
✅ 1. Flask-Based Web Server
Serves as the backend API for license key validation.

Built with Python and Flask.

Running locally on http://127.0.0.1:5000.

✅ 2. SQLite Database Integration
Stores all license keys with relevant metadata.

Each license record includes:

license_key

machine_id

expiry_date

status (optional: "valid", "expired", "revoked")

✅ 3. License Key Generation Script
generate_license.py creates unique license keys using UUID.

Inputs:

machine_id (user input)

validity in days (e.g., 180 days)

Automatically saves to the SQLite database using SQLAlchemy ORM.

✅ 4. License Key Validation
A web-based GUI form sends the key to the Flask API.

Server checks:

If key exists in DB

If the key is valid and not expired

If it matches the machine ID (coming soon)

Returns JSON response: "valid" or "invalid".

✅ 5. Browser-Based GUI
HTML form for users to enter and validate license keys.

Interacts with the server using POST requests.

Displays status to user on the same page.


⚙️ How to Use
1. 🔧 Run the Flask Server
bash
Copy code
cd license_manager_online/server
python app.py
Visit http://127.0.0.1:5000 in your browser.

2. 🔑 Generate a License Key
bash
Copy code
python generate_license.py
Enter:

Machine ID (e.g., MACHINE_001)

Validity in days (e.g., 180)

License key will be saved to the database and printed in the terminal.

3. ✅ Validate a License
Open the browser GUI → Paste the generated license key → Submit → See status.

📦 Technologies Used
Python 3.11+

Flask – Web framework

SQLite – Lightweight database

SQLAlchemy – ORM for database interaction

HTML/CSS – GUI template

📌 Coming Soon (Planned Features)
 Admin panel to view/add/delete licenses from browser

 GUI version of key generator

 Machine ID binding + enforcement

 Auto-expiry detection

 Secure online deployment (Render/AWS)

 PyInstaller packaging (.exe creation)

 License key encryption and signing

👤 Author
Anveshak Singh
Project under: Exeliq Tech Solutions
