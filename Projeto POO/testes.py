from classesmain import *

biblioteca = Biblioteca("Leitura")
douglas = Membro("Douglas","A1DF776M")
lucas = Membro("Lucas","4MN97PG")
livro1 = Livro("Diário de um Banana", "Douglas", "1ADF78")
livro2 = Livro("Senhor dos Áneis", "Chico Buarque", "2MGL93")
#Definicao de objetos

#teste catalogo
biblioteca.atualizar_catalogo([livro1, livro2])
#for livro in biblioteca.catalogo:
#    print(livro.titulo)
#biblioteca.atualizar_catalogo([livro1])

# teste adicionar membro
print(biblioteca.adicionar_membro(douglas))
print(biblioteca.adicionar_membro(lucas))
pedro = Membro("Pedro", "4MN97PG")
#pedro = Membro("Pedro", "AAAAAA")
print(biblioteca.adicionar_membro(pedro))

print(biblioteca.fazer_emprestimo(douglas, livro1))
print(biblioteca.fazer_emprestimo(lucas, livro1))
print(biblioteca.fazer_emprestimo(pedro, livro2))
print(livro1.status)
print(livro2.status)
print(biblioteca.devolver_livro(livro2))
print(biblioteca.devolver_livro(livro2))
biblioteca.pesquisar_livro("Diário de um Banana")
#testes de métodos