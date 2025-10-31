import os
from domain.entities.emprestimo import Emprestimo
from use_cases.verificar_emprestimo import VerificarEmprestimo

class InterfaceCLI:
    @staticmethod
    def limpar_tela():
        os.system('cls' if os.name == 'nt' else 'clear')

    def executar(self):
        self.limpar_tela()
        renda = float(input("Digite o valor da sua renda mensal: "))
        parcela = float(input("Digite o valor da parcela desejada: "))

        emprestimo = Emprestimo(renda, parcela)
        caso_uso = VerificarEmprestimo(emprestimo)
        resultado = caso_uso.executar()

        print(resultado)
