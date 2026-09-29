import sqlite3

def cadastrar_livro():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    titulo = input("Digite o título do livro: ")
    autor_id = int(input("Digite o ID do autor: "))
    editora_id = int(input("Digite o ID da editora: "))
    ano_publicacao = int(input("Digite o ano de publicação: "))
    edicao = int(input("Digite a edição: "))
    disponivel = int(input("Digite 1 se o livro estiver disponível ou 0 se não estiver: "))
    if disponivel == 1:
        disponivel = True
    elif disponivel == 0:
        disponivel = False
    else:
        print("Valor ínvalido! Digite 1 para disponível ou 0 para indisponível.")
        return

    cursor.execute("INSERT INTO livros (titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel) VALUES (?, ?, ?, ?, ?, ?)", (titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel)  )

    conn.commit()
    print("Livro cadastrado com sucesso!")

    conn.close()

