class Livro:
    def __init__(self, titulo: str, autor: str, ID: str) -> None:
        self.titulo = titulo
        self.autor = autor
        self.id = ID
        self.status = False

class Membro:
    def __init__(self, nome: str, id_membro: int) -> None:
        self.nome = nome
        self.id = id_membro
        self.historico = []

class Biblioteca:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.catalogo = []
        self.registros = {}
    
    def atualizar_catalogo(self, livros: list) -> None:
        """
        Adiciona livros ao catálogo verificando se eles já não existem
        """
        for livro in livros:
            if livro not in self.catalogo:
                self.catalogo.append(livro)
                print(f"Livro {livro.titulo} adicionado ao catálogo com sucesso.")
            else:
                print(f"{livro.titulo} já existe no catálogo. Tente outro.")

    def adicionar_membro(self, membro: object) -> str:
        """
        Cadastra membros a biblioteca verificando se o ID não é igual ao de outro membro.
        """
        if membro.id not in self.registros.keys():
            self.registros.update({membro.id: membro.nome})
            return f"{membro.nome} cadastrado na biblioteca com sucesso."
        
        else:
            return f"Já existe um ID igual nos registros."

    def fazer_emprestimo(self, membro: object, livro: object) -> str:
        """
        Verifica se o membro tem cadastro na biblioteca e se sim, adiciona o livro a seu historico de empréstimos.
        """
        if membro.id in self.registros.keys() and membro.nome in self.registros.values():
            
            if livro.status == False:
                membro.historico.append(livro)
                livro.status = True
                return f"Empréstimo realizado para {membro.nome}"
            else:
                return f"O livro {livro.titulo} já está emprestado. Retorne quando for devolvido." 
        
        else:
            return f"{membro.nome} não é cadastrado na biblioteca. Cadastre-se primeiro."
    
    def devolver_livro(self, livro: object) -> str:
        """
        Verifica se um livro já foi devolvido e se não, devolve e retorna uma string.
        """
        if livro.status == True:
            livro.status = False
            return f"{livro.titulo} devolvido a biblioteca."
        
        else:
            return f"{livro.titulo} já está na biblioteca."
    
    def pesquisar_livro(self, titulo: str) -> None:
        """
        Verifica se o livro existe no catálogo e se sim printa os atributos do livro
        """
        for livro in self.catalogo:
            if livro.titulo == titulo:
                print("Livro:")
                print(f"Nome: {livro.titulo}")
                print(f"Autor: {livro.autor}")
                print(f"ID: {livro.id}")
                print("Status:", "Dísponivel" if livro.status == False else "Em uso")
                break
        else:
            print(f"O livro {titulo} não está disponível na biblioteca.")