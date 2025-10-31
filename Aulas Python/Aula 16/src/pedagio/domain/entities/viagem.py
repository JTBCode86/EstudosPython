class Viagem:
    """Entidade responsável por representar uma viagem e calcular o valor do pedágio."""

    def __init__(self, distancia_km: float):
        if distancia_km < 0:
            raise ValueError("A distância não pode ser negativa.")
        self.distancia_km = distancia_km

    def calcular_pedagio(self) -> float:
        """Calcula o valor do pedágio com base na distância percorrida."""
        if self.distancia_km <= 100:
            return 10.0
        elif self.distancia_km <= 200:
            return 20.0
        else:
            return 30.0
