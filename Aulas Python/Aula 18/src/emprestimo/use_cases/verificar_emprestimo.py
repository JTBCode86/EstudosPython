from domain.entities.emprestimo import Emprestimo

class VerificarEmprestimo:
    def __init__(self, emprestimo: Emprestimo):
        self.emprestimo = emprestimo

    def executar(self) -> str:
        if self.emprestimo.renda_mensal <= 2000:
            return "Empréstimo negado: renda inferior a R$ 2.000,00."
        
        limite_parcela = self.emprestimo.renda_mensal * 0.3
        
        if self.emprestimo.valor_parcela > limite_parcela:
            return "Empréstimo negado: parcela acima de 30% da renda."
        
        return "Empréstimo aprovado!"
