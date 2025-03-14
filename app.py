from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import base64
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Configure Database (Using SQLite locally, switch to PostgreSQL for AWS)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alpr.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Database Model
class LicensePlate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(20), nullable=False)
    image = db.Column(db.Text, nullable=False)  # Store base64 image
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    country = db.Column(db.String(50), nullable=False)
    confidence = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<LicensePlate {self.plate}>"

# Create Database Tables
with app.app_context():
    db.create_all()

# Store latest ALPR data
latest_plate_data = None

@app.route('/alpr', methods=['POST'])
def receive_alpr_data():
    global latest_plate_data
    try:
        data = request.get_json()
        plate = data.get("plate")
        image = data.get("image")  # Base64 encoded
        date_str = data.get("date")
        country = data.get("country")
        confidence = data.get("confidence")

        # Convert date string to datetime
        date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")

        # Store in database
        new_entry = LicensePlate(
            plate=plate,
            image=image,
            date=date,
            country=country,
            confidence=confidence
        )
        db.session.add(new_entry)
        db.session.commit()

        # Update latest data for display
        latest_plate_data = {
            "plate": plate,
            "image": image,
            "date": date_str,
            "country": country,
            "confidence": confidence
        }

        return jsonify({"message": "License plate stored successfully", "plate": plate}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def display_latest_plate():
    # Get all entries from the database
    plates = LicensePlate.query.order_by(LicensePlate.date.desc()).all()

    return render_template("index.html", latest=latest_plate_data, plates=plates)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True, port=5000)
