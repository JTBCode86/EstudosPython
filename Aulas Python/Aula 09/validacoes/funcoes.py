import os

def limpa_tela():
     os.system('cls')
    
def escolha_operacao(escolha):
    if escolha ==1:
        msg = "Soma"
    elif escolha ==2:
        msg = "Subtração"
    elif escolha ==3:
        msg = "Multiplicação"
    elif escolha ==4:
        msg = "Divisão"

    print(f"\nVocê escolheu a opção {escolha} {msg}")
    
    a = input("Informe o primeiro valor: ")
    b = input("Informe o segundo valor: ")

    match escolha:
        case 1:
            return calc_adicao(a, b)
        case 2:
            return calc_subtracao(a, b)
        case 3:
            return calc_multiplicacao(a, b)
        case 4:
            return calc_divisao(a, b)
        case _:
            return "Número inválido."

def calc_adicao(a, b):
    try:
        return float(a) + float(b)
    except ValueError as ve:
        return f"Erro: Entrada inválida - {ve}"

def calc_subtracao(a, b):
    try:
        return float(a) - float(b)
    except ValueError as ve:
        return f"Erro: Entrada inválida - {ve}"

def calc_multiplicacao(a, b):
    try:
        return float(a) * float(b)
    except ValueError as ve:
        return f"Erro: Entrada inválida - {ve}"

def calc_divisao(a, b):
    try:
        a = float(a)
        b = float(b)
        if b == 0:
            return "Erro: Não é possível dividir por zero."
        return a / b
    except ValueError as ve:
        return f"Erro: Entrada inválida - {ve}"