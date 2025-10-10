from validacoes.funcoes import valida_qtd_vendas

def main():
    
    try:
        vendas_maca = input("Digite a quantidade de maçãs ventidas: ")
        vendas_banana = input("Digite a quantidade de bananas vendidas: ")

        produto_vencedor = valida_qtd_vendas(vendas_banana,vendas_maca)
        print(produto_vencedor)
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números inteiros.")

if __name__ =="__main__":
    main()