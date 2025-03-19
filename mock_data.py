from db_instance import db  # Import the database instance
from models import LicensePlateVA  # Import the model

from datetime import datetime
from db_instance import db  # Import the database instance
from models import LicensePlateVA  # Import the model

def insert_mock_data():

    # Insert mock data into the database
    record1 = LicensePlateVA(datetime=datetime(2025, 4, 1, 8, 15), plate="SKR9859E", make="Toyota", model="Corolla", color="White")
    record2 = LicensePlateVA(datetime=datetime(2025, 4, 1, 9, 30), plate="SGB267D", make="Honda", model="Civic", color="Black")
    record3 = LicensePlateVA(datetime=datetime(2025, 4, 1, 10, 45), plate="GBH1206B", make="Tesla", model="Model 3", color="Red")
    record4 = LicensePlateVA(datetime=datetime(2025, 4, 2, 12, 20), plate="GBL1368X", make="BMW", model="X5", color="Blue")
    record5 = LicensePlateVA(datetime=datetime(2025, 4, 2, 14, 50), plate="MKL8721Z", make="Mercedes-Benz", model="C-Class", color="Silver")
    record6 = LicensePlateVA(datetime=datetime(2025, 4, 2, 16, 10), plate="RXA4123M", make="Audi", model="A4", color="Gray")
    record7 = LicensePlateVA(datetime=datetime(2025, 4, 3, 8, 55), plate="TZX4589Q", make="Ford", model="Mustang", color="Yellow")
    record8 = LicensePlateVA(datetime=datetime(2025, 4, 3, 10, 30), plate="MLP7621D", make="Nissan", model="Altima", color="Brown")
    record9 = LicensePlateVA(datetime=datetime(2025, 4, 3, 11, 40), plate="QWE9876P", make="Hyundai", model="Tucson", color="Green")
    record10 = LicensePlateVA(datetime=datetime(2025, 4, 4, 13, 5), plate="XYZ1234M", make="Chevrolet", model="Camaro", color="Gold")
    record11 = LicensePlateVA(datetime=datetime(2025, 4, 4, 15, 15), plate="SKR9859E", make="Toyota", model="Corolla", color="White")
    record12 = LicensePlateVA(datetime=datetime(2025, 4, 4, 17, 20), plate="SGB267D", make="Honda", model="Civic", color="Black")
    record13 = LicensePlateVA(datetime=datetime(2025, 4, 5, 9, 10), plate="GBH1206B", make="Tesla", model="Model 3", color="Red")
    record14 = LicensePlateVA(datetime=datetime(2025, 4, 5, 11, 45), plate="GBL1368X", make="BMW", model="X5", color="Blue")
    record15 = LicensePlateVA(datetime=datetime(2025, 4, 5, 13, 50), plate="MKL8721Z", make="Mercedes-Benz", model="C-Class", color="Silver")
    record16 = LicensePlateVA(datetime=datetime(2025, 4, 6, 7, 30), plate="RXA4123M", make="Audi", model="A4", color="Gray")
    record17 = LicensePlateVA(datetime=datetime(2025, 4, 6, 10, 20), plate="TZX4589Q", make="Ford", model="Mustang", color="Yellow")
    record18 = LicensePlateVA(datetime=datetime(2025, 4, 6, 12, 40), plate="MLP7621D", make="Nissan", model="Altima", color="Brown")
    record19 = LicensePlateVA(datetime=datetime(2025, 4, 7, 14, 10), plate="QWE9876P", make="Hyundai", model="Tucson", color="Green")
    record20 = LicensePlateVA(datetime=datetime(2025, 4, 7, 16, 55), plate="XYZ1234M", make="Chevrolet", model="Camaro", color="Gold")
    record21 = LicensePlateVA(datetime=datetime(2025, 4, 7, 18, 30), plate="SKR9859E", make="Toyota", model="Corolla", color="White")
    record22 = LicensePlateVA(datetime=datetime(2025, 4, 8, 9, 15), plate="SGB267D", make="Honda", model="Civic", color="Black")
    record23 = LicensePlateVA(datetime=datetime(2025, 4, 8, 11, 00), plate="GBH1206B", make="Tesla", model="Model 3", color="Red")
    record24 = LicensePlateVA(datetime=datetime(2025, 4, 8, 13, 45), plate="GBL1368X", make="BMW", model="X5", color="Blue")
    record25 = LicensePlateVA(datetime=datetime(2025, 4, 8, 15, 20), plate="MKL8721Z", make="Mercedes-Benz", model="C-Class", color="Silver")

    # Add all records to the session
    db.session.add_all([
        record1, record2, record3, record4, record5, record6, record7, record8, record9, record10,
        record11, record12, record13, record14, record15, record16, record17, record18, record19, record20,
        record21, record22, record23, record24, record25
    ])

    # Commit the session to save records to the database
    db.session.commit()

    print("✅ 25 mock LicensePlateVA records inserted successfully.")
