# gerenciador de Listas de Compras

def exibir_menu():
    print("\n--- Menu ---")
    print("-- 1. Adicionar Item")
    print("-- 2. Remover item")
    print("-- 3. Lista itens")
    print("-- 4. Sair")

def adicionar_item(lista):
    item = input("Digite o nome do item a ser adicionado: ").strip()
    if item in lista:
        print(f"O item '{item}' já está na lista.")
    else:
        lista.append(item)
        print(f"Item '{item}' adicionado a lista com sucesso!!")

def remover_item(lista):
    item = input("Digite o nome do item a ser removido: ").strip()
    if item in lista:
        lista.remove(item)
        print(f"Item '{item}' removido da lista com sucesso!!")
    else:
        print(f"O item '{item}' não está na lista.")

def listar_itens(lista):
    if lista:
        print("\nItens na lista de compras: ")
        for i, item in enumerate(lista, start=1):
            print(f"{i}. {item}")
    else:
        print("A lista de compras está vazia.")

#programa principal
lista_compras = []

while True:
    exibir_menu()
    try:
        opcao = int(input("Escolha uma Opção: "))
    
        if opcao == 1:
            adicionar_item(lista_compras)
        elif opcao == 2:
            remover_item(lista_compras)
        elif opcao == 3:
            listar_itens(lista_compras)
        elif opcao == 4:
            print("Encerrando o Programa!")
            print("Boa Sorte com as suas Compras!!")
            break
        else:
            print("Opção Invalida! Tente novamente.")
    except ValueError:
        print("Entrada Invalida! Por favor, insira um número correspondente á opção.")