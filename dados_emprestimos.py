import sqlite3

def cadastrar_emprestimo():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()
    
    usuario_id = input("Digite o ID do usuário: ")

    cursor.execute("INSERT INTO emprestimos (usuario_id) VALUES (?)", (usuario_id,))
    conn.commit()
    print("Empréstimo cadastrado com sucesso!")

    conn.close()