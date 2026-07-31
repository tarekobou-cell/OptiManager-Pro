from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER
import os


def generer_facture_pdf(vente):

    nom_fichier = f"facture_{vente.id}.pdf"

    document = SimpleDocTemplate(
        nom_fichier,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    contenu = []


    # Logo

    logo_path = "utils/logo.png"

    if os.path.exists(logo_path):

        logo = Image(
            logo_path,
            width=4*cm,
            height=2*cm
        )

        contenu.append(logo)


    contenu.append(Spacer(1, 10))


    titre = Paragraph(
        "FACTURE OPTICIEN",
        styles["Title"]
    )

    contenu.append(titre)

    contenu.append(Spacer(1, 10))


    # Informations magasin

    infos = """
    OptiManager Optique<br/>
    Adresse : Votre adresse<br/>
    Téléphone : 05 XX XX XX XX
    """

    contenu.append(
        Paragraph(
            infos,
            styles["Normal"]
        )
    )


    contenu.append(Spacer(1,20))


    # Client

    contenu.append(
        Paragraph(
            f"<b>Client :</b> {vente.client_nom}",
            styles["Normal"]
        )
    )


    contenu.append(
        Paragraph(
            f"<b>Facture N° :</b> {vente.id}",
            styles["Normal"]
        )
    )


    contenu.append(Spacer(1,20))


    # Tableau

    data = [
        [
            "Désignation",
            "Qté",
            "Prix unité",
            "Total"
        ]
    ]


    for ligne in vente.lignes:

        data.append(
            [
                ligne.designation,
                ligne.quantite,
                f"{ligne.prix_unitaire:.2f} DA",
                f"{ligne.sous_total:.2f} DA"
            ]
        )


    table = Table(
        data,
        colWidths=[
            7*cm,
            2*cm,
            3*cm,
            3*cm
        ]
    )


    table.setStyle(
        TableStyle(
            [
                ("GRID",(0,0),(-1,-1),0.5,None),
                ("ALIGN",(1,1),(-1,-1),"CENTER"),
                ("ALIGN",(0,0),(-1,0),"CENTER"),
            ]
        )
    )


    contenu.append(table)


    contenu.append(Spacer(1,20))


    contenu.append(
        Paragraph(
            f"<b>TOTAL : {vente.total:.2f} DA</b>",
            styles["Heading2"]
        )
    )


    contenu.append(Spacer(1,40))


    contenu.append(
        Paragraph(
            "Signature et cachet",
            styles["Normal"]
        )
    )


    document.build(contenu)


    return nom_fichier
