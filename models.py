
from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from database import Base


class Sala(Base):
    __tablename__ = "salas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    capacidad: Mapped[int] = mapped_column(Integer, nullable=False)
    disponible: Mapped[bool] = mapped_column(Boolean, default=True)

    reservas: Mapped[list["Reserva"]] = relationship(back_populates="sala")


class Reserva(Base):
    __tablename__ = "reservas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    estudiante: Mapped[str] = mapped_column(String(100), nullable=False)
    sala_id: Mapped[int] = mapped_column(
    ForeignKey("salas.id"),
    nullable=False
)
    fecha: Mapped[str] = mapped_column(String(10), nullable=False)

    sala: Mapped["Sala"] = relationship(back_populates="reservas")
