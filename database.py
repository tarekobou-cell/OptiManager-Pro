"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : database.py
Description : Gestion centralisée de la base de données.
Auteur : Mohamed Tarek & ChatGPT
Version : 2.0.0
=========================================================
"""

from contextlib import contextmanager
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from models.base import Base


# =========================================================
# Chemins du projet
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

DATABASE_DIR = BASE_DIR / "database"
DATABASE_DIR.mkdir(parents=True, exist_ok=True)

DATABASE_PATH = DATABASE_DIR / "optique.db"

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"


# =========================================================
# Gestionnaire de base de données
# =========================================================

class DatabaseManager:
    """Gestionnaire central de la base de données."""

    def __init__(self) -> None:

        self.engine = create_engine(
            DATABASE_URL,
            echo=False,
            future=True,
        )

        self.SessionLocal = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def create_tables(self) -> None:
        """Crée toutes les tables."""

        Base.metadata.create_all(bind=self.engine)

    def get_session(self) -> Session:
        """Retourne une nouvelle session SQLAlchemy."""

        return self.SessionLocal()

    @contextmanager
    def session_scope(self):
        """
        Fournit une session avec commit / rollback automatique.
        """

        session = self.get_session()

        try:
            yield session
            session.commit()

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()


# =========================================================
# Instance globale
# =========================================================

db = DatabaseManager()

engine = db.engine

SessionLocal = db.SessionLocal