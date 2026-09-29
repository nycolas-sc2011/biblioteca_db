import sqlite3 as sqlite
from dados_usuarios import cadastrar_usuario
from dados_livros import cadastrar_livro
from dados_emprestimos import cadastrar_emprestimo
from dados_emprestimos_livro import cadastrar_emprestimo_livro
from dados_autores import cadastrar_autor
from dados_editoras import cadastrar_editora
from lista import listas_usuarios, listas_editoras, listas_emprestimos, listas_emprestimos_livros, listas_autores, listas_livros, listas_todas


while True:
    print("\n== mEnU dE oPçÕeS==")
    print("Escolha sua opção:")
    print("1. Cadastrar usuário")
    print("2. Cadastrar livro")
    print("3. Cadastrar empréstimo")
    print("4. Cadastrar empréstimo de livro")
    print("5. Cadastrar autor")
    print("6. Cadastrar editora")
    print("7. Listar usuários")
    print("8. Listar editoras")
    print("9. Listar empréstimos")
    print("10. Listar empréstimos de livros")
    print("11. Listar autor")
    print("12. Listar livro")
    print("13. Listar todas as informações")
    print("14. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '67':
        print("""
   666666    7777777777
  66    66          77
 66                77
 66666666         77
 66     66       77
 66     66      77
  666666       77
-------
Número completamente problemático, escolha outro.
    """)
        continue

    elif opcao == '1':
        cadastrar_usuario()
    elif opcao == '2':
        cadastrar_livro()
    elif opcao == '3':
        cadastrar_emprestimo()
    elif opcao == '4':
        cadastrar_emprestimo_livro()
    elif opcao == '5':
        cadastrar_autor()
    elif opcao == '6':
        cadastrar_editora()
    elif opcao == '7':
        listas_usuarios()
    elif opcao == '8':
        listas_editoras()
    elif opcao == '9':
        listas_emprestimos()
    elif opcao == '10':
        listas_emprestimos_livros()
    elif opcao == '11':
        listas_autores()
    elif opcao == '12':
        listas_livros()
    elif opcao == '13':
        listas_todas()
    elif opcao == '14':
        print("Tchau! Até breve!")
        break
    else:
        print("Opção inválida. Tente novamente.")

'''código pronto'''