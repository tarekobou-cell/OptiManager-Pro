from database import SessionLocal
from models.prescription import Prescription

db = SessionLocal()

prescriptions = db.query(Prescription).all()

for p in prescriptions:
    print(
        p.id,
        p.consultation_id,
        p.notes
    )

db.close()