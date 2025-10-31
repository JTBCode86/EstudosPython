import os
from use_cases.verificar_acesso import VerificarAcessoUseCase
from domain.entities.controle_acesso import ControleAcesso

class ControleAcessoCLI:
    """Interface de linha de comando para interação com o usuário."""

    def __init__(self):
        self.controle_acesso = ControleAcesso()
        self.use_case = VerificarAcessoUseCase(self.controle_acesso)

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def executar(self):
        self.limpar_tela()
        print("=== Sistema de Controle de Acesso ===")
        try:
            hora_atual = int(input("Informe a hora atual (0 a 23): "))
            mensagem = self.use_case.executar(hora_atual)
            print("\n" + mensagem)
        except ValueError as e:
            print(f"Erro: {e}")
