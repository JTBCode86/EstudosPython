from  somar.funcoes import somar_valores

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    resultado = somar_valores(numero1, numero2)
    print(f"A soma é: {resultado}")
except  ValueError:
        print('Erro: Digite apenas números validos!')

