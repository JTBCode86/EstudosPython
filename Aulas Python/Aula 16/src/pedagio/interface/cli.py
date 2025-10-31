import os
from use_cases.calcular_pedagio import CalcularPedagioUseCase

class PedagioCLI:
    """Interface de linha de comando para interação com o usuário."""

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def executar(self):
        self.limpar_tela()
        print("=== Sistema de Cálculo de Pedágio ===")
        try:
            distancia = float(input("Digite a distância percorrida (em km): "))
            use_case = CalcularPedagioUseCase(distancia)
            resultado = use_case.executar()
            print("\n" + resultado)
        except ValueError as e:
            print(f"Erro: {e}")
