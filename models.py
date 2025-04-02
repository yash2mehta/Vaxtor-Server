from datetime import datetime

# Import the database object
from db_instance import db

# Database Model for information retrieved from Vaxtor
class LicensePlateVaxtor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(20), nullable=False)
    image = db.Column(db.Text, nullable=False)  # Store base64 image
    datetime = db.Column(db.DateTime, nullable=False)
    country = db.Column(db.String(50), nullable=False)
    confidence = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<LicensePlate {self.plate}>"

# Database Model for information given to Vertical Adjustment System (by Vaxtor) - This was for testing purposes
class LicensePlateVA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, nullable=False)
    plate = db.Column(db.String(20), nullable=False) # This should not be unique as same car can enter checkpoint again
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(30), nullable=False)

# Database Model for information retrieved from Plate Recognizer
class LicensePlatePlateRecognizer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(20), nullable=False)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<LicensePlate {self.plate} - {self.make} {self.model}>"
