import os
from use_cases.verificar_paridade import VerificarParidadeUseCase

class ParidadeCLI:
    """Interface de linha de comando para verificar se um número é par ou ímpar."""

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def executar(self):
        self.limpar_tela()
        print("=== Verificador de Paridade ===")
        try:
            numero = int(input("Digite um número inteiro: "))
            use_case = VerificarParidadeUseCase(numero)
            resultado = use_case.executar()
            print("\n" + resultado)
        except ValueError as e:
            print(f"Erro: {e}")
