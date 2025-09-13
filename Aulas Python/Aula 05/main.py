from validaPalavras.validacoes import encontrar_palavras_longas

texto = input("Digite um texto: ")
palavras_longas = encontrar_palavras_longas(texto)

if palavras_longas:
    print("\nPalavras encontradas com mais de 10 letras: \n")
    contador = 0
    for palavra in palavras_longas:
        contador += 1
        print(f"{contador}. {palavra}")
else:
    print("\nNenhuma palavra com mais de 10 letras foi encontrada.")