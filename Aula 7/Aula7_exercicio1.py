#Big Data & IoT
import random

def gerar_dados_sensor(qtd_leitura):
    """
    Gera uma lista de leituras simulandas de um temperatura.
    cada leitura é um valor aleatório entre 15.0ºC e 35.0ºC, arredondado para duas casas decimais;
    """

    dados_sensor = [round(random.uniform(15.0, 45.0), 2) for _ in range(qtd_leitura)]
    return dados_sensor

def filtrar_temperatura_altas(dados_sensor, limite = 30.0):
    """
    filtrar e retorna as leituras cuja temperatura ultrapassa o valor limite
    """
    leituras_altas = [temperatura for temperatura in dados_sensor if temperatura > limite]
    return leituras_altas

def inserir_leitura_sensor(dados_sensor, nova_leitura, posicao = None):
    """
    insere uma nova leitura na lista de dados do sensor.
    se aposição não for especificada ou for invalida , a nova leitura é acionada ao final da lista.
    """
    if posicao is None or posicao >= len(dados_sensor):
        dados_sensor.append(nova_leitura)
    else:
        dados_sensor.insert(posicao, nova_leitura)
    return dados_sensor

def remover_leituras_anormais(dados_sensor, limite_inferior=15.0,limite_superior=30.0):
    """
    remove da lista de dadsoas leituras que estejam fora do intervalo definido pelos limites inferior e superios.
    """
    dados_limpos = [temperatura for temperatura in dados_sensor if limite_inferior <= temperatura <= limite_superior]
    return dados_limpos

def principal():
    quantidade_leitura = 10000 #número de leituras simuladas
    dados = gerar_dados_sensor(quantidade_leitura)
    print(f"Quantidade de leituras geradas: {len(dados)}")

    leituras_com_temperatura_alta = filtrar_temperatura_altas(dados, limite=30.0)
    print(f"Quantidade de leituras geradas acima de 30ºC: {len(leituras_com_temperatura_alta)}")
    
    nova_leitura = 28.5 #simula a adição de um novo sensor ao atualização de leitura
    dados = inserir_leitura_sensor(dados, nova_leitura)
    print(f"Quantidade de leituras após inserção: {len(dados)}")

    dados_limpos = remover_leituras_anormais(dados, limite_inferior=15.0, limite_superior=35.0)
    print(f"Quantidade de leituras após a remoção das anomalias: {len(dados_limpos)}")

if __name__ == "__main__":
    principal()
