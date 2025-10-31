from domain.entities.controle_acesso import ControleAcesso

class VerificarAcessoUseCase:
    """Caso de uso responsável por verificar o acesso com base na hora atual."""

    def __init__(self, controle_acesso: ControleAcesso):
        self.controle_acesso = controle_acesso

    def executar(self, hora_atual: int) -> str:
        """Executa a verificação e retorna a mensagem apropriada."""
        if self.controle_acesso.acesso_permitido(hora_atual):
            return "✅ Acesso permitido. Bem-vindo ao escritório!"
        else:
            return "❌ Acesso negado. O horário de entrada é entre 8h e 18h."
