from gorjeta.calcular import valor_total_gorjeta
from gorjeta.calcular import valor_total_pagar
 
total_conta = float(input('Digite o valor da conta: '))
porcentagem = float(input('Digite a porcentagem de gorjeta: '))
valor_final = valor_total_gorjeta(total_conta,porcentagem)

gorjeta = valor_total_gorjeta(total_conta,porcentagem)
valor_total = valor_total_pagar(total_conta,gorjeta)

print(f'Valor da gorjeta: R$ {round(gorjeta,2)}')
print(f'Total a pagar: R$ {round(valor_total,2)}')