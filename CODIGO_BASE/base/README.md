# Atividade Prática 02 - Biblioteca Persistente

Complete os arquivos da base usando SQLAlchemy ORM.

## Como executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Defesa escrita

Responda ao final:

1. Para que serve o campo `disponivel` em `Livro`?
para indicar se o livro está disponível
2. Por que é necessário chamar `session.commit()` após emprestar ou devolver?
para enviar ao banco as alterações
3. Em qual consulta você usa o relacionamento entre `Livro` e `Autor`?
def listar_livros_por_autor(session, nome_autor):
    """Liste os livros de um autor informado pelo nome."""
    # TODO: busque o autor e navegue por autor.livros.
    consulta = ((select(Livro).join(Autor).where(Livro.autor_id) ==(Autor.id)))
    return session.scalars(consulta).all()

Utilizei o relacionamento para dar um join entre as duas tabelas

