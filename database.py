from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


# ---------------------------------------------------------------------
# Dossiers du projet
# ---------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATABASE_DIR = BASE_DIR / "database"
DATABASE_DIR.mkdir(exist_ok=True)

DATABASE_PATH = DATABASE_DIR / "optique.db"


# ---------------------------------------------------------------------
# Base SQLAlchemy
# ---------------------------------------------------------------------

class Base(DeclarativeBase):
    pass


# ---------------------------------------------------------------------
# Connexion SQLite
# ---------------------------------------------------------------------

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True,
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)