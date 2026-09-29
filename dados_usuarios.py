import sqlite3

def cadastrar_usuario():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()
    
    nome = input("Digite o nome do usuário: ")

    cursor.execute("INSERT INTO usuarios (nome) VALUES (?)", (nome,))
    conn.commit()
    print("Usuário cadastrado com sucesso!")

    conn.close()