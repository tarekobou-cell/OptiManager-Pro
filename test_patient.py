import sys

from PySide6.QtWidgets import QApplication

from ui.patients.liste_patients import ListePatients


app = QApplication(sys.argv)

fenetre = ListePatients()

fenetre.resize(800, 500)

fenetre.show()

sys.exit(app.exec())
