def valida_vogais(frase):
    vogal='aeiou'
    frase_minuscula = frase.lower()
    contar_vogal = 0
    for letra in frase_minuscula:
        if letra in vogal:
            contar_vogal += 1
    return contar_vogal