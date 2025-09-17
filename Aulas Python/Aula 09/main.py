import os,sys
from validacoes.funcoes import escolha_operacao 
from validacoes.funcoes import limpa_tela

def main():
    while True:
        limpa_tela()
        print("\nBem vindo a calculadora Pyton 1.0.")
        print("\nEscolha uma operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")

        try:
            escolha = int(input("Digite sua escolha: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue

        if escolha == 0:
            print("Saindo do programa.")
            break

        resultado = escolha_operacao(escolha)

        print(f"Resultado: {resultado}\n")
        input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()