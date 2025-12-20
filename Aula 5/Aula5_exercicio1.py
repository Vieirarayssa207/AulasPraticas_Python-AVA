# agenda de contatos
import json
import os

#se estiver testando o codigo, coloque as linhas 7 e 8 em comentarios, 
#por que elas só valem para a minha maquina
CAMINHO_BASE = r"C:\Projetos\Atividade Python\Aulas praticas em PYthon - AVA\Aula 5"
ARQUIVO_CONTATOS = os.path.join(CAMINHO_BASE, "contatos.json")
#e estiver tentato estar o arquivo tire o # (do cometario)  da linha 11,
#e deixxe somente o codigo.
#ARQUIVO_CONTATOS =  "contatos.json"

def carregar_contatos():
    if os.path.exists(ARQUIVO_CONTATOS):
        try:
            with open(ARQUIVO_CONTATOS, "r", encoding="UTF-8")  as arquivos:
                return json.load(arquivos)
        except json.JSONDecodeError:
            print("ERROR: ao carregar os contatos. o arquivo pode ser corompido!")
            return {}
    return {}

def salvar_contatos(contatos):
    with open(ARQUIVO_CONTATOS, "w", encoding="UTF-8") as arquivos:
        json.dump(contatos, arquivos, indent=4, ensure_ascii=False)

def adicionar_contato(contatos):
    nome = input("Digite o nome do contato: ").strip()
    if nome in contatos:
        print(f"O contato Já existe.")
        return
    
    telefone = input("Digite o numero de telefone: ").strip()
    email = input("Digite o email: ").strip()

    contatos[nome] = {"telefone": telefone, "email": email}
    salvar_contatos(contatos)
    print(f"Contato '{nome}' adicionado com sucesso!")

def remover_contato(contatos):
    nome = input("Digite o nome do contato a ser removido: ").strip()
    if nome in contatos:
        del contatos[nome]
        salvar_contatos(contatos)
        print(f"O contato '{nome}' foi removido com sucesso!")
    else:
       print(f"O contato '{nome}' não foi encontrado.")

def listar_contatos(contatos):
    if contatos:
        print("\nLista de Contato:")
        for nome, dados in contatos.items():
            print(f"Nome: {nome}, Telefone: {dados['telefone']}, e-mail: {dados['email']}")
    else:
        print("Nenhum contato Cadastrado!")

def exibir_menu():
    print("="*50)
    print("-"*10," Programa de Contatos ","-"*10)
    print("-"*18," Menu ","-"*18)
    print("|","-" * 5," 1. Adicionar um contato")
    print("|","-" * 5," 2. Remover um contato")
    print("|","-" * 5," 3. Listar os contatos")
    print("|","-" * 5," 4. Sair")
    print("="*50)

# Programa Principal
contatos = carregar_contatos()

while True:
    exibir_menu()
    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            adicionar_contato(contatos)
        elif opcao == 2:
            remover_contato(contatos)
        elif opcao == 3:
            listar_contatos(contatos)
        elif opcao == 4:
            print("Encerrando o Programa!")
            print("Seus contatos foram salvos!")
            print("Está salvos no arquivo 'contatos.json'.")
            break
        else:
            print("Opção Invalida! Tente novamente.")
    except ValueError:
        print("Entrada Invalida! Por favor, insira um número correspondente á opção.")