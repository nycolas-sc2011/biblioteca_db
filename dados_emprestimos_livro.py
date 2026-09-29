import sqlite3
from datetime import datetime

def cadastrar_emprestimo_livro():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    emprestimo_id = int(input("Digite o ID do empréstimo: "))
    livro_id = int(input("Digite o ID do livro: "))
    data_devolucao_str = input("Digite a data de devolução (dd/mm/aaaa): ")
    data_devolucao = datetime.strptime(data_devolucao_str, "%d/%m/%Y")

    cursor.execute(
        "INSERT INTO emprestimos_livros (emprestimo_id, livro_id, data_devolucao) VALUES (?, ?, ?)",
        (emprestimo_id, livro_id, data_devolucao)
    )
    
    conn.commit()
    print("Empréstimo de livro cadastrado com sucesso!")

    conn.close()
'''código pronto'''