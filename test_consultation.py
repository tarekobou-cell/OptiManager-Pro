import models.patient
import models.consultation
import models.prescription

from services.consultation_service import creer_consultation


c = creer_consultation(
    patient_id=1,
    motif="Contrôle vision",
    observations="Nouvelle correction"
)

print(c.id, c.date_consultation)