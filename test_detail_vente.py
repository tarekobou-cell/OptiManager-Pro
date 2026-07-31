from services.vente_service import detail_vente


vente = detail_vente(5)


print("Client :", vente.client_nom)
print("Total :", vente.total)


print("---- Lignes ----")

for ligne in vente.lignes:

    print(
        ligne.designation,
        "x",
        ligne.quantite,
        "=",
        ligne.sous_total
    )