#Robótica e os Veículos Autônomos
import time
import random

def gerar_tarefas(qtd_tarefas):
    tarefas = []
    sensores = ["LIDAR","câmera","ultrassônico"]
    prioridades = ["alta","media","baixa"]
    for i in range(1, qtd_tarefas + 1):
        tarefa = {
            "id": i,
            "descricao": f"Processar dados do sensor {random.choice(sensores)}",
            "prioridade": random.choice(prioridades)
        }
        tarefas.append(tarefa)
    return tarefas

def adicionar_tarefa(fila_tarefas, tarefa):
    fila_tarefas.append(tarefa)
    return fila_tarefas

def processar_tarefa(fila_tarefas):
    if len(fila_tarefas) > 0:
        tarefa = fila_tarefas.pop(0)
        print(f"Processando tarefas ID: {tarefa['id']}, Descrição: {tarefa['descricao']}, Prioridade: {tarefa['prioridade']}")
        time.sleep(1)
    else:
        print("Nenhuma tarefa para procesar.")
    return fila_tarefas

def principal():
    qtd_inicial_tarefas = 5
    fila_tarefas = gerar_tarefas(qtd_inicial_tarefas)
    print("Fila inicial de tarefas:")
    for tarefa in fila_tarefas:
        print(tarefa)

    print("\nProcessamento das tarefas em tempo real:")
    while fila_tarefas:
        fila_tarefas = processar_tarefa(fila_tarefas)
    nova_tarefa = {
        "id": qtd_inicial_tarefas + 1,
        "descricao": "Processar dados do sensor GPS",
        "prioridade": "alta"
    }
    fila_tarefas = adicionar_tarefa(fila_tarefas, nova_tarefa)
    print("\nNova Tarefa adicionada. Fila atual:")
    print(fila_tarefas)

    print("\nProcessando a nova tarefa:")
    fila_tarefas = processar_tarefa(fila_tarefas)

if __name__ == "__main__":
    principal()