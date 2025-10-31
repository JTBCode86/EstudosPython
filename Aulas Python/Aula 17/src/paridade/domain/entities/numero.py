class Numero:
    """Entidade que representa um número e permite verificar sua paridade."""

    def __init__(self, valor: int):
        if not isinstance(valor, int):
            raise ValueError("O valor deve ser um número inteiro.")
        self.valor = valor

    def eh_par(self) -> bool:
        """Retorna True se o número for par, False se for ímpar."""
        return self.valor % 2 == 0
