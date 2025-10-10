
def valida_qtd_vendas(vendas_banana,vendas_maca):
    
    if  vendas_banana > vendas_maca:
        return f"O produto mais fendido foram as banandas com a quantidade de {vendas_banana} vendidas no total."
    elif vendas_maca > vendas_banana:
        return f"O produto mais fendido foram as maças com a quantidade de {vendas_maca} vendidas no total."
    else:  
        resultado = vendas_banana
        return f"Amobos os produtos tiveram a mesma quantidade de vendas sendo {vendas_banana} bananas e {vendas_maca} maças vendidos no total."      