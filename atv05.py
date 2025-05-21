from random import randint

class ContaBancaria:
    def __init__(self):
        self.__saldo = 0
        self.__numConta = randint(1, 9999)

    def __str__(self):
        return f'Saldo: {self.__saldo} | Número da conta: {self.__numConta}'

    def mostrar_saldo(self):
        return f'O seu saldo é R${self.__saldo}'
    
    def mostrar_numConta(self):
        return f'O número da conta é {self.__numConta}'
    
    def depositar(self, valorAdicionado):
        if valorAdicionado > 0:
            self.__saldo += valorAdicionado 
            return f'Saldo de R${valorAdicionado} adicionado com sucesso. '
        else:
            return 'Operação inválida. '
        
    def sacar(self):
        opcoes = [20, 50, 100]
        for i, opcao in enumerate(opcoes):
            print(f'{i + 1} - R${opcao}')
        print()
        try:
            opcaoDeSaque = int(input("Digite o índice do valor a sacar: "))
            if 1 <= opcaoDeSaque <= 3:
                valor_saque = opcoes[opcaoDeSaque - 1]
                if self.__saldo >= valor_saque:
                    self.__saldo -= valor_saque
                    return f"Saque de R${valor_saque} realizado com sucesso."
                else:
                    return "Saldo insuficiente para saque."
            else:
                return "Opção inválida!"
        except ValueError:
            return "Entrada inválida. Digite um número válido."

def menu():
    cliente1 = ContaBancaria()
    while True:
        opcao = input(''''

    (1) - Ver número da conta
    (2) - Ver saldo
    (3) - Depositar
    (4) - Sacar
    (5) - Sair

''')
        match opcao:
            case '1':
                print(cliente1.mostrar_numConta())
            case '2':
                print(cliente1.mostrar_saldo())
            case '3':
                try:
                    valorDepositado = float(input("Digite o valor a ser adicionado: "))
                    print(cliente1.depositar(valorDepositado))
                except ValueError:
                    print("Digite um valor válido!")
            case '4':
                print(cliente1.sacar())
            case '5':
                print("Deslogando sua conta...")
                break
            case _:
                print("Digite uma opção válida! ")

menu()
