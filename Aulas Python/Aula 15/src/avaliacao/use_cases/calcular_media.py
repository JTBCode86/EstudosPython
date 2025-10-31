from domain.entities.aluno import Aluno

class CalcularMediaUseCase:
    """Caso de uso para calcular média e determinar a situação do aluno."""

    def __init__(self, notas: list[float]):
        self.aluno = Aluno(notas)

    def executar(self) -> str:
        media = self.aluno.calcular_media()
        situacao = self.aluno.situacao()
        return f"Média: {media:.2f}\n{situacao}"
