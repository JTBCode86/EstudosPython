def valida_cpf(numero_cpf):
    if len(numero_cpf)> 11 or len(numero_cpf)< 11:
        print('Erro: O CPF deve ter exatamente 11 dígitos.')
    elif not numero_cpf.isnumeric():
        print('Erro: O CPF deve conter apenas números.')
    else:
        print('CPF Valido.')      

