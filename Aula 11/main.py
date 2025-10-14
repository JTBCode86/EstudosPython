from validacoes.funcoes import limpar_tela
from validacoes.funcoes import validar_temperatura

def main():
    temperatura = input('Digite a temperatura atual: ')
    resultado = validar_temperatura(temperatura)
    limpar_tela()
    print(resultado)

if __name__ =="__main__":
    main()