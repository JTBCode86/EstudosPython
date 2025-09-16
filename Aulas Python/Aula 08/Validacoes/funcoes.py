import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    
    while True:

        try:
            palpite = int(input("Tente adivinhar o número (1-100): "))

            if palpite < 1 or palpite > 100:
                raise ValueError("O número deve estar entre 1 e 100.")
            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print("Parabéns! Você acertou!")
                break
            
        except ValueError as ve:
            print(f"Entrada inválida: {ve}")    