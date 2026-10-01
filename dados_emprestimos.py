import sqlite3
import datetime as dt

def cadastrar_emprestimo():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    usuario_id = input("Digite o ID do usuário: ")

    data_emprestimo = dt.datetime.strptime(
        input("Digite a data do empréstimo (DD/MM/AAAA): "),
        "%d/%m/%Y"
    ).date()

    cursor.execute(
        "INSERT INTO emprestimos (usuario_id, data_emprestimo) VALUES (?, ?)",
        (usuario_id, data_emprestimo)
    )

    conn.commit()

    print("Empréstimo cadastrado com sucesso!")

    conn.close()
'''código pronto'''
