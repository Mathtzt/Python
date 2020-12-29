##Esse arquivo foi criado para o estudo das Coleções no python em especial as listas e tuplas.

class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} saldo {}<<]".format(self.codigo, self.saldo)

##Trecho para facilitar testes
def init_lista_contas():
    conta_pessoal = ContaCorrente(10)
    conta_pessoal.deposita(500)
    ##print(conta_pessoal)

    conta_da_maria = ContaCorrente(11)
    conta_da_maria.deposita(1000)

    return [conta_pessoal, conta_da_maria]

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

def testes_tuplas():
    """
    Quando queremos trabalhar que posições específicas significam coisas diferentes, ou seja, a estrutura da minha sequencia deve permanecer a mesma no momento que foi inicializada, isso já é indício do uso de um tupla ao invés de uma lista.
    """
    conta_pessoal = ('Matheus', 25, 1995) ##Inicializando uma tupla. Obs: Note que usamos o parênteses para isso.
    #conta_pessoal.append(123) ##Quebrará porque uma tupla é uma representação imutável.


##################################
if (__name__ == "__main__"):
    ##Testando lista de objetos
    contas = init_lista_contas()
    for conta in contas:
        print(conta)

    ##Depositando 100 reais em todas as contas
    deposita_para_todas(contas)
    print(contas[0], contas[1])


