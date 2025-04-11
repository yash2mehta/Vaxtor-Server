from flask import jsonify, render_template
from app.models import LicensePlatePlateRecognizer
from app.extensions import db

def init_routes(app):
    @app.route('/home/platerecognizer')
    def display_latest_plate_platerecognizer():
        plates = LicensePlatePlateRecognizer.query.all()
        return render_template("index-platerecognizer.html", plates=plates)

    @app.route('/platerecognizer-record-latest', methods=['GET'])
    def retrieve_latest_record_platerecognizer():
        latest_record = LicensePlatePlateRecognizer.query.order_by(LicensePlatePlateRecognizer.id.desc()).first()

        if not latest_record:
            return jsonify({"error": "No records found in database"}), 404

        result = {
            "id": latest_record.id,
            "plate": latest_record.plate,
            "make": latest_record.make,
            "model": latest_record.model
        }

        return jsonify(result), 200 