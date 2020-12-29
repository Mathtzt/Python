##Esse arquivo foi criado para o estudo das Coleções no python em especial as listas e tuplas.
from abc import ABCMeta, abstractmethod, ABC


class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return "[>>Codigo {} saldo {}<<]".format(self._codigo, self._saldo)

class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass

### Testes
if (__name__ == "__main__"):
    ## 1
    print("\nTeste 1")
    conta1 = ContaCorrente(1)
    conta1.deposita(1000)
    conta1.passa_o_mes()
    print(conta1)

    ## 2
    print("\nTeste 2")
    conta2 = ContaPoupanca(2)
    conta2.deposita(1000)
    conta2.passa_o_mes()
    print(conta2)

    ## 3 - Utilizando o polimorfismo com a listas
    print("\nTeste 3")
    conta1 = ContaCorrente(1)
    conta1.deposita(1000)
    conta2 = ContaPoupanca(2)
    conta2.deposita(1000)
    contas = [conta1, conta2]

    for conta in contas:
        conta.passa_o_mes() #duck typing
        print(conta)

    ## 4 - Forçando um metodo abstrato. Objetivo é dar um erro mostrando que é necessário implementar o método passa_o_mes
    print("\nTeste 4")
    ContaInvestimento()