from domain.entities.orcamento import Orcamento

class VerificarOrcamentoUseCase:
    def __init__(self, orcamento: Orcamento):
        self.orcamento = orcamento

    def executar(self, total_despesas: float) -> str:
        self.orcamento.adicionar_despesas(total_despesas)
        if self.orcamento.esta_dentro_do_limite():
            saldo = self.orcamento.obter_saldo()
            return f"Você ainda está dentro do orçamento. Saldo restante: R$ {saldo:.2f}"
        else:
            excesso = abs(self.orcamento.obter_saldo())
            return f"Atenção! Você ultrapassou o limite em R$ {excesso:.2f}"
