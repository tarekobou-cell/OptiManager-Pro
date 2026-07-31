import models.patient
import models.consultation
import models.rendez_vous
import models.prescription

from services.prescription_service import creer_prescription


p = creer_prescription(
    consultation_id=1,
    od_sphere=-1.25,
    od_cylindre=-0.50,
    od_axe=90,
    og_sphere=-1.00,
    og_cylindre=-0.25,
    og_axe=80,
    addition="+2.00",
    notes="Verres progressifs"
)

print(
    p.id,
    p.od_sphere,
    p.og_sphere
)