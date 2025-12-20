#controle de gastos mensais
def calcular_saldo(rendimento, despesas):
    return rendimento - despesas

def sugerir_poupanca(saldo):
    return saldo * 0.2

#entrada de dados
try:
    rendimento = float(input("Digite seu rendimento mensal (em reais): R$ "))
    if rendimento < 0:
        raise ValueError("O rendimeto não pode ser negativo")
    
    despesas = float(input("Digite o total de suas despesas mensais (em reais): R$ "))
    if despesas < 0:
        raise ValueError("As despesas não pode ser negativo")
    
    tem_poupanca = input("Você tem poupança? (sim/não): ").strip().lower()
    if tem_poupanca not in ["sim","não"]:
        raise ValueError("Respoata Inválida!! Digite igualmente uma das duas opções: 'sim' ou 'não'.")

    # Processamento
    saldo = calcular_saldo(rendimento, despesas)
    print(f"\nSeu saldo mensal é: R$ {saldo:,.2f}")
    if saldo < 0:
        print("Atenção!! Suas despesas estão maiores que seus rendimentos.")
    elif saldo > 0:
        if tem_poupanca == "sim":
            poupanca_sugerir = sugerir_poupanca(saldo)
            print(f"Recomendamos poupar R$ {poupanca_sugerir:,.2f} esse mês.")
        else:
            print("Considere criar um plano de poupança para aproveitar seu saldo positivo.")
        
except ValueError as e:
    print(f"ERROR!!! entrada de dados {e} está errada!!!")