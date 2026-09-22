# Biblioteca_bd




Implementação do exemplo clássico da Biblioteca salvando os dados em um banco de dados sqlite.

As tabelas do projeto são:

**usuarios**(_id, nome_)  
**autores**(_id, nome_)  
**editoras**(_id, nome_)  
**livros**(_id, titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel_)  
**emprestimos**(_d, usuario_id, data_)  
**emprestimos_livros**(_emprestimo_id, livro_id, data_devolucao_)  

Em dupla, implemente a aplicação com menu de opções de cadastro e listagem para cada tabela do modelo.

Publicar nesta tarefa o link para o repositório no github.
