from models import Autor, Livro
from faker import Fake
from sqlalchemy.orm import Session
from database import *
f = Fake()
def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""
    with Session(engine) as session:
        autor1 = Autor(nome = 'Hugo', pais = 'Venezuela',)
        autor2 = Autor(nome = 'Marcos', pais = 'Espanha',)
        autor3 = Autor(nome = 'Lucas', pais = 'China',)
        session.add(autor1, autor2, autor3)
        session.commit()
        livro = Livro(titulo = 'Dom Quixote ', ano = 1605, autor_id = 1, disponivel = False)
        livro2 = Livro(titulo = 'Orgulho e Preconceito ', ano = 1322, autor_id = 1, disponivel = True)
        livro3 = Livro(titulo = 'Frankenstein  ', ano = 1818, autor_id = 2, disponivel = True)
        livro4 = Livro(titulo = 'Crime e Castigo ', ano = 1866, autor_id = 3, disponivel = False)
        livro5 = Livro(titulo = 'Guerra e Paz ', ano = 1869, autor_id = 1, disponivel = False)
        livro6 = Livro(titulo = '1984  ', ano = 1949, autor_id = 1, disponivel = False)
        session.add(livro,livro2,livro3,livro4,livro5,livro6)
        session.commit()


