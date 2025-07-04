from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///licenses.db'
db = SQLAlchemy(app)

class License(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    license_key = db.Column(db.String(32), unique=True, nullable=False)
    machine_id = db.Column(db.String(64), nullable=False)
    expiry = db.Column(db.String(10), nullable=False)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/validate', methods=['GET', 'POST'])
def validate():
    if request.method == 'POST':
        license_key = request.form.get('license_key')
        machine_id = request.form.get('machine_id')
    else:
        data = request.get_json()
        license_key = data.get('license_key')
        machine_id = data.get('machine_id')

    license = License.query.filter_by(license_key=license_key, machine_id=machine_id).first()
    
    if not license:
        result = "Invalid license."
    else:
        today = datetime.today().date()
        expiry = datetime.strptime(license.expiry, "%Y-%m-%d").date()
        if today <= expiry:
            result = "License is VALID."
        else:
            result = "License has EXPIRED."

    if request.method == 'POST':
        return render_template('index.html', result=result)
    else:
        return jsonify({'status': result.lower(), 'expiry': license.expiry if license else None})

if __name__ == '__main__':
    app.run(debug=True)


