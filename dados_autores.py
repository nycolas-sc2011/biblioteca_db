
import sqlite3

def cadastrar_autor():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()
    
    nome = input("Digite o nome do autor: ")

    cursor.execute("INSERT INTO autores (nome) VALUES (?)", (nome,))
    conn.commit()
    print("Autor cadastrado com sucesso!")

    conn.close()