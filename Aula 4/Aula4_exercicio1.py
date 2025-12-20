#Gerenciador de Tarefas Diárias
def exibir_menu():
    print("\n--- Menu ---")
    print("-- 1. Adicionar Tarefa")
    print("-- 2. Remover Tarefa")
    print("-- 3. Lista de Tarefas")
    print("-- 4. Lista de Tarefas Concluidas")
    print("-- 5. Sair")

def adicionar_tarefa(lista_tarefas):
    tarefa = input("Digite a descrição de uma tarefa: ").strip()
    if any(tarefa == item['descricao'] for item in lista_tarefas):
        print(f"A tarefa '{tarefa}' já está na lista.")
    else:
        lista_tarefas.append({"descricao": tarefa, "concluida": False})
        print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def marcar_concluida(lista_tarefas):
    tarefa = input("Digite a descrição de uma tarefa a ser mardada como concluída: ").strip()
    for item in lista_tarefas:
        if item["descricao"] == tarefa:
            if item["concluida"]:
                print(f"A tarefa '{tarefa}' já está marcada como concluida.")
            else:
                item["concluida"] = True
                print(f"Tarefa '{tarefa}' foi marcada como concluida com sucesso!")
            return
    print(f"Tarefa '{tarefa}' não encontrda na lista.")


def listar_tarefas(lista_tarefas, concluida):
    status = "concluida" if concluida else "pendentes"
    tarefas = [item["descricao"] for item in lista_tarefas if item["concluida"] == concluida]

    if tarefas:
        print(f"\nTarefas {status}:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")
    else:
        print(f"Não há tarefas {status} no momento.")

# Programa Principal
lista_tarefas = []

while True:

    exibir_menu()
    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            adicionar_tarefa(lista_tarefas)
        elif opcao == 2:
            marcar_concluida(lista_tarefas)
        elif opcao == 3:
            listar_tarefas(lista_tarefas, concluida=False)
        elif opcao == 4:
            listar_tarefas(lista_tarefas, concluida=True)
        elif opcao == 5:
            print("Encerrando o Programa!")
            print("Boa Sorte com suas Tarefas!!")
            break
        else:
            print("Opção Invalida! Tente novamente.")
    except ValueError:
        print("Entrada Invalida! Por favor, insira um número correspondente á opção.")