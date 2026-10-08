from sqlalchemy import select

from models import Autor, Livro


def listar_livros(session):
    """Liste todos os livros com o nome do autor e o status de disponibilidade."""
    # TODO: use select(Livro) e acesse livro.autor.nome.
    consulta = select(Livro.autor.nome)
    consulta2 = select(Livro.disponibilidade)
    return print(consulta, consulta2)

    


def listar_livros_disponiveis(session):
    """Liste apenas os livros disponíveis."""
    # TODO: filtre Livro.disponivel igual a True.
    consulta = (select(Livro).where(Livro.disponivel)) == True
    return session.scalars(consulta).all()

    


def buscar_livros_por_titulo(session, trecho):
    """Busque livros por parte do título."""
    # TODO: use contains ou like no título.
    consulta = ((select(Livro).where(Livro.titulo).like("Dom %")))
    return session.scalars(consulta).all()


def listar_livros_por_autor(session, nome_autor):
    """Liste os livros de um autor informado pelo nome."""
    # TODO: busque o autor e navegue por autor.livros.
    consulta = ((select(Livro).join(Autor).where(Livro.autor_id) ==(Autor.id)))
    return session.scalars(consulta).all()
