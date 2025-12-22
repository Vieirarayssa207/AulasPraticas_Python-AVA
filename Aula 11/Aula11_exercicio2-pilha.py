#Sistemas de Atendimento
import time

def gerar_requisicoes(qtd_requisicoes):
    requisicoes = []
    nomes_clientes = ["Cliente_A","Cliente_B","Cliente_C","Cliente_D"]
    problemas = ["Problemas de conexão", "Erro no sistema", "Dúvida sobre faturamento", "Solicitação de suporte"]
    for i in range(1, qtd_requisicoes + 1):
        requisicao = {
            "id": i,
            "cliente": nomes_clientes[i % len(nomes_clientes)],
            "problema": problemas[i % len(problemas)],
            "horario": f"{time.strftime('%H:%M:%S')}"
        }
        requisicoes.append(requisicao)
        time.sleep(0.1)
    return requisicoes

def adicionar_requisicao(pilha_requisicoes, nova_requisicao):
    pilha_requisicoes.append(nova_requisicao)
    return pilha_requisicoes

def processar_requisicao(pilha_requisicoes):
    if pilha_requisicoes:
        requisicao = pilha_requisicoes.pop() #aqui está a diferança: pop() sem argumento
        print(f"Processando requisição ID: {requisicao['id']} | Cliente: {requisicao['cliente']} | Problema: {requisicao['problema']} | Horário: {requisicao['horario']}")
        time.sleep(1)
    else:
        print("Nenhuma requisição para processar.")
    return pilha_requisicoes

def principal():
    qtd_inicial_requisicoes = 5
    pilha_requisicoes = gerar_requisicoes(qtd_inicial_requisicoes)
    print("Fila inicial de requisições:")
    for requisicao in pilha_requisicoes:
        print(requisicao)

    print("\nProcessamento das requisições em ordem:")
    while pilha_requisicoes:
        pilha_requisicoes = processar_requisicao(pilha_requisicoes)
    
    nova_requisicao = {
        "id": qtd_inicial_requisicoes + 1,
        "cliente": "Cliente_E",
        "problema": "Reclamação de atraso no serviço",
        "horario": f"{time.strftime('%H:%M:%S')}"
    }
    pilha_requisicoes = adicionar_requisicao(pilha_requisicoes, nova_requisicao)
    print("\nNova requisição adicionada. Fila atual:")
    print(pilha_requisicoes)

if __name__ == "__main__":
    principal()