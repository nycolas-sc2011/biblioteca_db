import sqlite3
conn = sqlite3.connect("biblioteca.db")

def tabela_autores():
    conn.execute("CREATE TABLE if not exists autores (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

def tabela_editoras():
    conn.execute("CREATE TABLE if not exists editoras (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

def tabela_usuarios():
    conn.execute("CREATE TABLE if not exists usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

def tabela_livros():
    conn.execute("CREATE TABLE IF NOT EXISTS livros (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, autor_id INTEGER REFERENCES autores(id), editora_id INTEGER REFERENCES editoras(id), ano_publicacao INTEGER, edicao INTEGER, disponivel BOOLEAN)")

def tabela_emprestimos():
    conn.execute("CREATE TABLE if not exists emprestimos (id INTEGER PRIMARY KEY AUTOINCREMENT, usuario_id INTEGER REFERENCES usuarios(id), data DATE DEFAULT CURRENT_DATE)")

def tabela_emprestimos_livros():
    conn.execute("""
        CREATE TABLE IF NOT EXISTS emprestimos_livros (
            emprestimo_id INTEGER REFERENCES emprestimos(id),
            livro_id INTEGER REFERENCES livros(id),
            data_devolucao DATE,
            PRIMARY KEY (emprestimo_id, livro_id),
            FOREIGN KEY (emprestimo_id) REFERENCES emprestimos(id),
            FOREIGN KEY (livro_id) REFERENCES livros(id)
        )
    """)

tabela_autores()
tabela_editoras()
tabela_usuarios()
tabela_livros()
tabela_emprestimos()
tabela_emprestimos_livros()

conn.commit()
conn.close()
