from datetime import datetime

import models.patient
import models.consultation
import models.rendez_vous

from services.rendez_vous_service import (
    creer_rendez_vous,
    liste_rendez_vous
)


rdv = creer_rendez_vous(
    patient_id=1,
    date_heure=datetime.now(),
    motif="Contrôle vision"
)


print(
    "RDV créé :",
    rdv.id,
    rdv.motif,
    rdv.statut
)


for r in liste_rendez_vous():

    print(
        r.id,
        r.patient_id,
        r.date_heure,
        r.motif,
        r.statut
    )