from services.vente_service import detail_vente
from utils.facture_pdf import generer_facture_pdf


vente = detail_vente(1)

fichier = generer_facture_pdf(vente)

print("Facture créée :", fichier)