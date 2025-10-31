import os
from use_cases.verificar_orcamento import VerificarOrcamentoUseCase
from domain.entities.orcamento import Orcamento

class OrcamentoCLI:
    def __init__(self):
        self.limite = 3000.0
        self.orcamento = Orcamento(self.limite)
        self.use_case = VerificarOrcamentoUseCase(self.orcamento)

    def limpar_tela(self):
        """Limpa o terminal de forma compatível com Windows e Unix."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def executar(self):
        self.limpar_tela()  # <-- chamada logo no início
        print("=== Controle de Orçamento Mensal ===")
        try:
            total = float(input("Informe o total de despesas realizadas (R$): "))
            resultado = self.use_case.executar(total)
            print(resultado)
        except ValueError as e:
            print(f"Erro: {e}")
