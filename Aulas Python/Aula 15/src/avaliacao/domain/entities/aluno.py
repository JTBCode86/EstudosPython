class Aluno:
    """Entidade que representa um aluno e suas notas."""

    def __init__(self, notas: list[float]):
        if len(notas) != 3:
            raise ValueError("Devem ser informadas exatamente três notas.")
        self.notas = notas

    def calcular_media(self) -> float:
        """Calcula e retorna a média das notas."""
        return sum(self.notas) / len(self.notas)

    def situacao(self) -> str:
        """Retorna a situação do aluno com base na média."""
        media = self.calcular_media()
        if media >= 7:
            return "Aprovado"
        elif media >= 5:
            return "Recuperação"
        else:
            return "Reprovado"
