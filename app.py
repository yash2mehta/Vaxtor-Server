from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import base64
import os

# Import the database object
from db_instance import db

# Import the models
from models import LicensePlateVaxtor, LicensePlateVA

# Import mock_data function
from mock_data import insert_mock_data

app = Flask(__name__)
CORS(app) # Allow cross-origin requests

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alpr.db' # Configure Database Using SQLite locally
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Store latest ALPR data for Vaxtor
latest_plate_data = None

# Initialize SQLAlchemy for the Flask app
db.init_app(app)

# POST request to send mock data to server (simulating Vaxtor)
## TODO - Need to add field for MMC, according to Vaxtor's JSON reporting variable
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
        datetime = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")

        # Store in database
        new_entry = LicensePlateVaxtor(
            plate=plate,
            image=image,
            datetime = datetime,
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


# GET Request to retrieve all mock data from database for vertical adjustment system
@app.route('/va-all', methods=['GET'])
def retrieve_all_records_va():
    records = LicensePlateVA.query.all()  # Fetch all records
    results = [
        {
            "id": record.id,
            "datetime": record.datetime.strftime("%Y-%m-%d %H:%M:%S"),
            "plate": record.plate,
            "make": record.make,
            "model": record.model,
            "color": record.color
        }
        for record in records
    ]
    return jsonify(results), 200  # Return JSON response



# GET Request to retrieve mock data for a specific id from database for vertical adjustment system
@app.route('/va-record/<int:record_id>', methods=['GET'])
def retrieve_specific_record_va(record_id):
    # Fetch record by ID
    record = LicensePlateVA.query.get(record_id)

    # If record is not found or ID is invalid, fetch the latest record
    if not record:
        record = LicensePlateVA.query.order_by(LicensePlateVA.id.desc()).first()

    # If no records exist in the database
    if not record:  
        return jsonify({"error": "No records found in database"}), 404

    result = {
        "id": record.id,
        "datetime": record.datetime.strftime("%Y-%m-%d %H:%M:%S"),
        "plate": record.plate,
        "make": record.make,
        "model": record.model,
        "color": record.color
    }

    return jsonify(result), 200  # Return JSON response


# GET Request to retrieve the latest record from the database for the vertical adjustment system
@app.route('/va-record-latest', methods=['GET'])
def retrieve_latest_record_va():
    
    # Fetch the latest record
    latest_record = LicensePlateVA.query.order_by(LicensePlateVA.id.desc()).first()

    # If no records exist in the database
    if not latest_record:
        return jsonify({"error": "No records found in database"}), 404

    result = {
        "id": latest_record.id,
        "datetime": latest_record.datetime.strftime("%Y-%m-%d %H:%M:%S"),
        "plate": latest_record.plate,
        "make": latest_record.make,
        "model": latest_record.model,
        "color": latest_record.color
    }

    return jsonify(result), 200  # Return JSON response


# Homepage showing results from database (for ALPR - Vaxtor)
@app.route('/home/alpr')
def display_latest_plate_alpr():
    # Get all entries from the database
    plates = LicensePlateVaxtor.query.order_by(LicensePlateVaxtor.date.desc()).all()

    return render_template("index-vaxtor.html", latest=latest_plate_data, plates=plates)


# Homepage showing results from database (for VA - Vertical Adjustment System)
@app.route('/home/VA')
def display_latest_plate_va():
    # Get all entries from the database
    plates = LicensePlateVA.query.order_by(LicensePlateVA.datetime.desc()).all()
    return render_template("index-va.html", latest=latest_plate_data, plates=plates)


if __name__ == "__main__":

    with app.app_context():

        # Drop all tables to start fresh
        db.drop_all()

        # Create database tables
        db.create_all() 

        # Insert mock data
        insert_mock_data()  

    app.run(host = '0.0.0.0', debug=True, port=5000)
