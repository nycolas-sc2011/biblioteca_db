import sqlite3

def cadastrar_editora():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()
    
    nome = input("Digite o nome da editora: ")

    cursor.execute("INSERT INTO editoras (nome) VALUES (?)", (nome,))
    conn.commit()
    print("Editora cadastrada com sucesso!")

    conn.close()