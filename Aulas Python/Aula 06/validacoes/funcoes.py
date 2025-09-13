import random
import string
import os

def gerar_senha(tamanho=12):
    if tamanho < 4:
        raise ValueError("O tamanho da senha deve ser pelo menos 4 caracteres.")

    letras_maiusculas = random.choice(string.ascii_uppercase)
    letras_minusculas = random.choice(string.ascii_lowercase)
    numeros = random.choice(string.digits)
    especiais = random.choice("!@#$%&*?")

    todos_caracteres = string.ascii_letters + string.digits + "!@#$%&*?"
    restantes = [random.choice(todos_caracteres) for _ in range(tamanho - 4)]

    senha_lista = list(letras_maiusculas + letras_minusculas + numeros + especiais) + restantes
    random.shuffle(senha_lista)

    senha = ''.join(senha_lista)
    return senha

def criterios_senha():
    print('\nSua senha respeita os seguintes critérios:')
    print("I.  12 caracteres")
    print("II. 1 letra minuscula")
    print("II. 1 número")
    print("IV. 1 caractere especial (de !@#$%&*?)")

def limpar_tela():
    os.system('cls')
