import sys

from PySide6.QtWidgets import QApplication

from ui.patients.fiche_patient import FichePatient


app = QApplication(sys.argv)

fenetre = FichePatient()

fenetre.resize(600, 700)

fenetre.show()

sys.exit(app.exec())