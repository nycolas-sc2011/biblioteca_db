import sqlite3

def cadastrar_livro():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    titulo = input("Digite o título do livro: ")
    autor_id = int(input("Digite o ID do autor: "))
    editora_id = int(input("Digite o ID da editora: "))
    ano_publicacao = int(input("Digite o ano de publicação: "))
    edicao = int(input("Digite a edição: "))
    while True:
        try:
            disponivel = int(input("Digite 1 se o livro estiver disponível ou 0 se não estiver: "))
        except ValueError:
            print("Valor inválido! Digite 1 para disponível ou 0 para indisponível.")
            continue

        if disponivel in (0, 1):
            disponivel = bool(disponivel)
            break

        print("Valor inválido! Digite 1 para disponível ou 0 para indisponível.")

    cursor.execute("INSERT INTO livros (titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel) VALUES (?, ?, ?, ?, ?, ?)", (titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel)  )

    conn.commit()
    print("Livro cadastrado com sucesso!")

    conn.close()

