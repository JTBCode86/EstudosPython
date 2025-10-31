from domain.entities.viagem import Viagem

class CalcularPedagioUseCase:
    """Caso de uso responsável por calcular o pedágio a partir da distância."""

    def __init__(self, distancia_km: float):
        self.viagem = Viagem(distancia_km)

    def executar(self) -> str:
        valor = self.viagem.calcular_pedagio()
        return f"Valor do pedágio: R$ {valor:.2f}"
