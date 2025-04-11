from app.extensions import db

class LicensePlatePlateRecognizer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(20), nullable=False)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<LicensePlate {self.plate} - {self.make} {self.model}>" 