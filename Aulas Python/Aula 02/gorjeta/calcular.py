def valor_total_gorjeta(total_conta,porcentagem):
    gorjeta=(total_conta*porcentagem)/100
    return gorjeta
    
def valor_total_pagar(total_conta,gorjeta): 
    return total_conta + gorjeta