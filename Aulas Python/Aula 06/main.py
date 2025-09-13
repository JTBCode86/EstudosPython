import os
from validacoes.funcoes import gerar_senha
from validacoes.funcoes import criterios_senha
from validacoes.funcoes import limpar_tela

def main():
    resposta = input("Deseja gerar uma senha? (sim/não): ").strip().lower()
    
    if resposta =="sim":
        limpar_tela()
        senha_gerada = gerar_senha()
        print("\nA senha gerada foi:", senha_gerada)
        criterios_senha()
    elif resposta == "não":
        limpar_tela()
        print("\nTudo bem. Até a próxima!")
    else:
        limpar_tela()
        print("\nResposta inválida. Por favor, digite 'sim' ou 'não'.")

if __name__ == "__main__":
    limpar_tela()
    main()