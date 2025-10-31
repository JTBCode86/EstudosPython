from domain.entities.numero import Numero

class VerificarParidadeUseCase:
    """Caso de uso responsável por verificar se um número é par ou ímpar."""

    def __init__(self, numero: int):
        self.numero = Numero(numero)

    def executar(self) -> str:
        if self.numero.eh_par():
            return f"O número {self.numero.valor} é par."
        else:
            return f"O número {self.numero.valor} é ímpar."
