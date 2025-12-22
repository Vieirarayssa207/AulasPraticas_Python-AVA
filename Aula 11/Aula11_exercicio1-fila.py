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

def adicionar_requisicao(fila_requisicoes, nova_requisicao):
    fila_requisicoes.append(nova_requisicao)
    return fila_requisicoes

def processar_requisicao(fila_requisicoes):
    if fila_requisicoes:
        requisicao = fila_requisicoes.pop(0)
        print(f"Processando requisição ID: {requisicao['id']} | Cliente: {requisicao['cliente']} | Problema: {requisicao['problema']} | Horário: {requisicao['horario']}")
        time.sleep(1)
    else:
        print("Nenhuma requisição para processar.")
    return fila_requisicoes

def principal():
    qtd_inicial_requisicoes = 5
    fila_requisicoes = gerar_requisicoes(qtd_inicial_requisicoes)
    print("Fila inicial de requisições:")
    for requisicao in fila_requisicoes:
        print(requisicao)

    print("\nProcessamento das requisições em ordem:")
    while fila_requisicoes:
        fila_requisicoes = processar_requisicao(fila_requisicoes)
    
    nova_requisicao = {
        "id": qtd_inicial_requisicoes + 1,
        "cliente": "Cliente_E",
        "problema": "Reclamação de atraso no serviço",
        "horario": f"{time.strftime('%H:%M:%S')}"
    }
    fila_requisicoes = adicionar_requisicao(fila_requisicoes, nova_requisicao)
    print("\nNova requisição adicionada. Fila atual:")
    print(fila_requisicoes)

if __name__ == "__main__":
    principal()