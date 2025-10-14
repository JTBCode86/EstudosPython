import os

def validar_temperatura(temperatura):

    if int(temperatura) > 25:
        return f'Alerta! Temperatura acima do limite permitido.'
    elif int(temperatura) < 0:
        return f'Alerta! Temperatura abaixo do limite mínimo.'
    else:
        return f'Temperatura dentro do limite permitido.'

def limpar_tela():
    os.system('cls')    