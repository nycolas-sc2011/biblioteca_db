def listas_usuarios():
    import sqlite3 as sqlite

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")

    resultados = cursor.fetchall()

    if not resultados:
        print("\nLista vazia.")
    else:
        for linha in resultados:
            print(f"id: {linha['id']} | nome: {linha['nome']}")

    conn.close() 

def listas_livros():
    import sqlite3 as sqlite

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")

    resultados = cursor.fetchall()

    if not resultados:
        print("\nLista vazia.")
    else:
        for linha in resultados:
            print(f"id: {linha['id']} | titulo: {linha['titulo']} | autor_id: {linha['autor_id']} | editora_id: {linha['editora_id']} | ano_publicacao: {linha['ano_publicacao']} | edicao: {linha['edicao']} | disponivel: {linha['disponivel']}")

    conn.close()

def listas_autores():
    import sqlite3 as sqlite

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM autores")

    resultados = cursor.fetchall()

    if not resultados:
        print("\nLista vazia.")
    else:
        for linha in resultados:
            print(f"id: {linha['id']} | nome: {linha['nome']}")

    conn.close()

def listas_editoras():
    import sqlite3 as sqlite

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM editoras")

    resultados = cursor.fetchall()
    if not resultados:
        print("\nLista vazia.")
    else:
        for linha in resultados:
            print(f"id: {linha['id']} | nome: {linha['nome']}")

    conn.close()

def listas_emprestimos():
    import sqlite3 as sqlite

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM emprestimos")

    resultados = cursor.fetchall()

    if not resultados:
        print("\nLista vazia.")
    else:
        for linha in resultados:
            print(f"id: {linha['id']} | usuario_id: {linha['usuario_id']} | data_emprestimo: {linha['data_emprestimo']}")

    conn.close()

def listas_emprestimos_livros():
    import sqlite3 as sqlite

    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM emprestimos_livros")

    resultados = cursor.fetchall()

    if not resultados:
        print("\nLista vazia.")
    else:
        for linha in resultados:
            print(f"emprestimo_id: {linha['emprestimo_id']} | livro_id: {linha['livro_id']} | data_devolucao: {linha['data_devolucao']}")

    conn.close()

def listas_todas():
    print("Lista de usuários:")
    listas_usuarios()
    print("\nLista de livros:")
    listas_livros()
    print("\nLista de autores:")
    listas_autores()
    print("\nLista de editoras:")
    listas_editoras()
    print("\nLista de empréstimos:")
    listas_emprestimos()
    print("\nLista de empréstimos de livros:")
    listas_emprestimos_livros()

'''código pronto'''