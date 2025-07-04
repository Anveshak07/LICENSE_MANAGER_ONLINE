from app import app, db, License
from datetime import datetime, timedelta
import uuid

license_key = str(uuid.uuid4()).replace("-", "").upper()[:16]
machine_id = "MACHINE_002"
expiry = (datetime.now() + timedelta(days=180)).strftime('%Y-%m-%d')

# Run inside Flask app context
with app.app_context():
    new_license = License(
        license_key=license_key,
        machine_id=machine_id,
        expiry=expiry
    )
    db.session.add(new_license)
    db.session.commit()

print("✅ New license added to database:")
print(f"License Key: {license_key}")
print(f"Machine ID : {machine_id}")
print(f"Expiry     : {expiry}")
