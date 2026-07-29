import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QMainWindow

from database import Base
from database import engine

import models.utilisateur


Base.metadata.create_all(bind=engine)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("OptiManager Pro")

        self.resize(1000, 700)

        label = QLabel(
            "Bienvenue dans OptiManager Pro !",
            self
        )

        label.move(40, 40)


app = QApplication(sys.argv)

window = MainWindow()

window.show()

sys.exit(app.exec())