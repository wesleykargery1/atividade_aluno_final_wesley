from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base, db


class Autor(Base):
    __tablename__ = "autores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    pais: Mapped[str]


    # TODO: relacione Autor com Livro usando relationship e back_populates.
    livro:Mapped[List['Livro']] = db.relationship(back_populates='autores')

class Livro(Base):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str]
    ano: Mapped[int]
    autor_id: Mapped[int] = mapped_column(ForeignKey("autores.id"))
    disponivel: Mapped[bool] = mapped_column(default=True)

    # TODO: adicione o campo disponivel, com valor padrão True.
    # TODO: relacione Livro com Autor usando relationship e back_populates.
    autor:Mapped['Autor'] = db.relationship(back_populates='livros')
