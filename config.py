from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

DATABASE_DIR = BASE_DIR / "database"

DATABASE_DIR.mkdir(exist_ok=True)


DATABASE_PATH = DATABASE_DIR / "optique.db"


DATABASE_URL = f"sqlite:///{DATABASE_PATH}"