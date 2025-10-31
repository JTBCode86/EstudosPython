import os
from use_cases.calcular_media import CalcularMediaUseCase

class AvaliacaoCLI:
    """Interface CLI para entrada de notas e exibição do resultado."""

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def executar(self):
        self.limpar_tela()
        print("=== Sistema de Avaliação de Alunos ===")
        try:
            notas = []
            for i in range(1, 4):
                nota = float(input(f"Digite a {i}ª nota: "))
                notas.append(nota)

            use_case = CalcularMediaUseCase(notas)
            resultado = use_case.executar()
            print("\n" + resultado)

        except ValueError as e:
            print(f"Erro: {e}")
