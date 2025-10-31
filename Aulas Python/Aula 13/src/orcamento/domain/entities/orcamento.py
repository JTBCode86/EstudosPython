class Orcamento:
    def __init__(self, limite: float):
        self.limite = limite
        self.despesas = 0.0

    def adicionar_despesas(self, valor: float):
        if valor < 0:
            raise ValueError("O valor da despesa não pode ser negativo.")
        self.despesas += valor

    def esta_dentro_do_limite(self) -> bool:
        return self.despesas <= self.limite

    def obter_saldo(self) -> float:
        return self.limite - self.despesas
