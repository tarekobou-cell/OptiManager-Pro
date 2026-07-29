from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox
)

from sqlalchemy.orm import Session

from database import SessionLocal
from models.utilisateur import Utilisateur
from utils.securite import verifier_mot_de_passe

from ui.dashboard import DashboardWindow


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.dashboard = None

        self.setWindowTitle(
            "Connexion - OptiManager Pro"
        )

        self.resize(400, 300)

        self.creer_interface()


    def creer_interface(self):

        self.titre = QLabel(
            "OptiManager Pro"
        )

        self.login_input = QLineEdit()
        self.login_input.setPlaceholderText(
            "Nom utilisateur"
        )

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText(
            "Mot de passe"
        )

        self.password_input.setEchoMode(
            QLineEdit.Password
        )

        self.btn_connexion = QPushButton(
            "Se connecter"
        )

        self.btn_connexion.clicked.connect(
            self.connexion
        )


        layout = QVBoxLayout()

        layout.addWidget(self.titre)
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.btn_connexion)

        self.setLayout(layout)


    def connexion(self):

        login = self.login_input.text()
        password = self.password_input.text()

        db: Session = SessionLocal()

        utilisateur = db.query(Utilisateur).filter(
            Utilisateur.login == login
        ).first()


        if utilisateur:

            mot_de_passe_correct = verifier_mot_de_passe(
                password,
                utilisateur.mot_de_passe
            )


            if mot_de_passe_correct:

                self.dashboard = DashboardWindow(
                    utilisateur
                )

                self.dashboard.show()

                self.close()


            else:

                QMessageBox.warning(
                    self,
                    "Erreur",
                    "Mot de passe incorrect"
                )


        else:

            QMessageBox.warning(
                self,
                "Erreur",
                "Utilisateur introuvable"
            )


        db.close()