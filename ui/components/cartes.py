from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)


class CarteStatistique(QWidget):

    def __init__(self, titre, valeur):
        super().__init__()

        self.titre = titre
        self.valeur = valeur

        self.creer_interface()


    def creer_interface(self):

        layout = QVBoxLayout()

        titre = QLabel(
            self.titre
        )

        valeur = QLabel(
            str(self.valeur)
        )

        layout.addWidget(titre)
        layout.addWidget(valeur)

        self.setLayout(layout)