from sqlalchemy import Integer, Float, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class LigneVente(Base):

    __tablename__ = "lignes_vente"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    vente_id: Mapped[int] = mapped_column(
        ForeignKey("ventes.id")
    )

    produit_id: Mapped[int] = mapped_column(
        ForeignKey("produits.id")
    )

    designation: Mapped[str] = mapped_column(
        String(150)
    )

    quantite: Mapped[int] = mapped_column(
        Integer
    )

    prix_unitaire: Mapped[float] = mapped_column(
        Float
    )

    sous_total: Mapped[float] = mapped_column(
        Float
    )


    vente = relationship(
        "Vente",
        back_populates="lignes"
    )