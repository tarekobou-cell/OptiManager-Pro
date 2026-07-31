from sqlalchemy import Integer, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Produit(Base):

    __tablename__ = "produits"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    reference: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    designation: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    categorie: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    # Monture / Verre / Accessoire

    traitement: Mapped[str] = mapped_column(
        String(50),
        nullable=True
    )
    # HC / HMC / Blue Block / Progressif...

    fournisseur: Mapped[str] = mapped_column(
        String(100),
        nullable=True
    )

    quantite: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    prix_achat: Mapped[float] = mapped_column(
        Float,
        default=0
    )

    prix_vente: Mapped[float] = mapped_column(
        Float,
        default=0
    )