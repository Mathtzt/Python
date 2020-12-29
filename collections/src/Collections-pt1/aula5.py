##Esse arquivo foi criado para o estudo das Coleções no python em especial as listas e tuplas.
"""
Builtins como enumerated, range e desempacotamento automatico de tuplas
"""
from functools import total_ordering

idades = [15, 87, 32, 65, 56, 32, 49, 37]

##usando só o que já conhecemos para mostrar index e valor
print("\nTeste 1")
for i in range(len(idades)):
    print(i, idades[i])

##usando o builtin enumerated
print("\nTeste 2")
enumerate(idades) # lazy...
print(list(enumerate(idades))) # forçando a geração dos valores

#melhorando o uso
print("\nTeste 3")
for indice, idade in enumerate(idades): # unpacking da tupla
    print("Indice {} - Idade {}".format(indice, idade))

##ordenação basica - sorted (crescente). Gera uma nova lista
print("\nTeste 4")
print(sorted(idades))

##ordenação basica - sorted (decrescente). Gera uma nova lista
print("\nTeste 5")
print(sorted(idades, reverse=True))

##ordenação basica - reversed (inverte os valores). Gera um iterável
print("\nTeste 6")
print(reversed(idades))

##caso deseje alterar, ordenando a lista principal (in place)
print("\nTeste 7")
idades2 = [15, 87, 32, 65, 56, 32, 49, 37]
idades2.sort()
print(idades2)

##ordenação de objetos através do __lt__ (lessthan)
"""
O functools, total_ordering, fornece todas as ordenações a partir da implementação de pelo menos os métodos eq e o lt.
Desse modo, eu consigo fazer comparações de <=, >= etc..
"""
@total_ordering
class ContaSalario():

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __eq__(self, outro):
        if type(outro != ContaSalario):
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro):
        return self._saldo < outro._saldo

    def __str__(self):
        return "[>>Codigo {} saldo {}<<]".format(self._codigo, self._saldo)


print("\nTeste 8")
conta_pessoal = ContaSalario(10)
conta_pessoal.deposita(250)
conta_mae = ContaSalario(12)
conta_mae.deposita(500)
conta_pai = ContaSalario(8)
conta_pai.deposita(450)

contas = [conta_pessoal, conta_mae, conta_pai]
for conta in sorted(contas): ## mostrando ordenação
    print(conta)

print("\nTeste 9")
for conta in sorted(contas, reverse=True): ## mostrando ordenação invertida
    print(conta)