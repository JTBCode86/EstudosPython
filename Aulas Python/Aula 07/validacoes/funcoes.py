import os
import random
    
def limpar_tela():
    os.system('cls')

def titulo_jogo():
    print(f"Bem-vindo ao jogo: Pedra, Papel e Tesoura!\n")

def jogar():
    opcoes = ['pedra', 'papel', 'tesoura']

    while True:
        jogador = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()

        if jogador == 'sair':
            limpar_tela()
            print("Obrigado por jogar!")
            break

        if jogador not in opcoes:
            limpar_tela()
            titulo_jogo()
            print("Opção inválida. Tente novamente.\n")
            continue

        computador = random.choice(opcoes)
        limpar_tela()
        titulo_jogo()
        print(f"Computador escolheu: {computador}")

        if jogador == computador:
            print("Empate! Essa foi por pouco")
        elif (jogador == 'pedra' and computador == 'tesoura') or \
             (jogador == 'papel' and computador == 'pedra') or \
             (jogador == 'tesoura' and computador == 'papel'):
            print("Você venceu! Parabéns")
        else:
            print("Você perdeu! hahaha")
        print()