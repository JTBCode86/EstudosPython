import string

def encontrar_palavras_longas(texto):
    texto_limpo = texto.translate(str.maketrans('', '', string.punctuation))    
    palavras = texto_limpo.split()
    palavras_longas=[palavra for palavra in palavras if len(palavra)>10]
    return palavras_longas