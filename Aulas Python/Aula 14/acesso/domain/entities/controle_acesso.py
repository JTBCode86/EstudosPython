class ControleAcesso:
    """Entidade responsável pelas regras de negócio do controle de acesso."""

    def __init__(self, hora_inicio: int = 8, hora_fim: int = 18):
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim

    def acesso_permitido(self, hora_atual: int) -> bool:
        """Retorna True se o horário estiver dentro do intervalo permitido."""
        if not (0 <= hora_atual <= 23):
            raise ValueError("Hora inválida! Use um valor entre 0 e 23.")
        return self.hora_inicio <= hora_atual <= self.hora_fim
