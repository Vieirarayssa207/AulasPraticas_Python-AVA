#Sistema de Biblioteca
class Livros:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False

    def __str__(self):
        status = "Emprestado" if self.emprestado else "Disponível"
        return f"{self.titulo} - {self.autor} ({status})"
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livros(self, titulo, autor):
        self.livros.append(Livros(titulo,autor))
        print(f"Livros '{titulo}' adicionado à biblioteca.")

    def listar_livros_disponiveis(self):
        disponiveis = [livro for livro in self.livros if not livro.emprestado]
        if disponiveis:
            print("\nLivros disponiveis:")
            for livro in disponiveis:
                print(f"- {livro}") 
        else:
            print("Nenhum livro disponivel no momento.")
    
    def listar_livros_emprestados(self):
        emprestados = [livro for livro in self.livros if livro.emprestado]
        if emprestados:
            print("\nLivros Emprestados:")
            for livro in emprestados:
                print(f"- {livro}") 
        else:
            print("Nenhum livro emprestado no momento.")

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                if not livro.emprestado:
                    livro.emprestado = True
                    print(f"Livro '{titulo}' emprestado com sucesso")
                else:
                    print(f"O livro '{titulo}' já está emprestado")
                return
        print(f"O livro '{titulo}' não foi encontrado na biblioteca.")

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                if livro.emprestado:    
                    livro.emprestado = False
                    print(f"Livro '{titulo}' devolvido com sucesso.")
                else:
                    print(f"O livro '{titulo}' não estava emprestado")
                return
        print(f"O livro '{titulo}' não foi encontrado na biblioteca.")
        
def exibir_menu():
    print("="*45)
    print("-"*20," BIBLIOTECA ","-"*20)
    print("-"*22," M E N U ","-"*21)
    print("|","-"*5," 1. Adicionar um livro")
    print("|","-"*5," 2. Listar os livros disponiveis")
    print("|","-"*5," 3. Listar os livros emprestados")
    print("|","-"*5," 4. Emprestar um Livro")
    print("|","-"*5," 5. Devolver um Livro")
    print("|","-"*5," 6. Sair")

#programa principal

Biblioteca = Biblioteca() 

while True:
    exibir_menu()
    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            titulo = input("Digite o título do livro: ").strip()
            autor = input("Digite o autor do livro: ").strip()
            Biblioteca.adicionar_livros(titulo, autor)
        elif opcao == 2:
            Biblioteca.listar_livros_disponiveis()
        elif opcao == 3:
            Biblioteca.listar_livros_emprestados()
        elif opcao == 4:
            titulo = input("Digite o título de livro a ser emprestado: ").strip()
            Biblioteca.emprestar_livro(titulo)
        elif opcao == 5:
            titulo = input("Digite o título de livro a ser devolvido: ").strip()
            Biblioteca.devolver_livro(titulo)
        elif opcao == 6:            
            print("<3 "*11)
            print("")
            print("Encerrando o Programa!")
            print("Volte sempre a nossa biblioteca!")
            print("")
            print("<3 "*11)
            break
        else:
            print("Opção Invalida! Tente novamente.")
    except ValueError:
        print("Entrada Invalida! Por favor, insira um número correspondente á opção.")