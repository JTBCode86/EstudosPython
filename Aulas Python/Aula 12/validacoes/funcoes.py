import os

def calcular_imc(peso, altura):
    
    """
    Calcula o Índice de Massa Corporal (IMC).

    Args:
        peso (float): O peso da pessoa em quilogramas (kg).
        altura (float): A altura da pessoa em metros (m).

    Returns:
        float: O valor do IMC calculado.
    """
    
    if altura <= 0:
        return "Erro: A altura deve ser um valor positivo maior que zero."

    # Fórmula do IMC: peso / (altura * altura)
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    """
    Classifica o IMC de acordo com as faixas de referência.

    Args:
        imc (float): O valor do IMC.

    Returns:
        str: A classificação do IMC.
    """
    # Retorna a mensagem de erro se o IMC for uma string de erro
    if isinstance(imc, str):
        return imc 

    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25.0 <= imc < 29.9:
        return "Sobrepeso"
    elif 30.0 <= imc < 34.9:
        return "Obesidade Grau I"
    elif 35.0 <= imc < 39.9:
        return "Obesidade Grau II (severa)"
    else:
        return "Obesidade Grau III (mórbida)"

def limpar_tela():
    os.system('cls')
