from validacoes.funcoes import calcular_imc
from validacoes.funcoes import classificar_imc
from validacoes.funcoes import limpar_tela

def main():

    limpar_tela()
    print("--- Calculadora de Índice de Massa Corporal (IMC) ---")
    
    try:
         # Pede o peso e converte para float
        peso_str = input("Digite seu peso em quilogramas (ex: 70.5): ")
        peso = float(peso_str.replace(',', '.')) 

        # Pede a altura e converte para float
        altura_str = input("Digite sua altura em metros (ex: 1.75): ")
        altura = float(altura_str.replace(',', '.')) 

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite números válidos para peso e altura.")
        return

    # Calcula o IMC
    imc = calcular_imc(peso, altura)

    # Imprime o erro de altura zero ou negativa
    if isinstance(imc, str):
        print(imc) 
    else:
        # Classifica e exibe o resultado
        classificacao = classificar_imc(imc)

        # Exibe o IMC com 2 casas decimais
        print(f"\nSeu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")

if __name__ =="__main__":
    main()
