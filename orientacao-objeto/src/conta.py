class Conta:
    ##construtor no python... manter o parametro self inserido pelo python que significa o endereço de memória que será gravado o objeto criado
    def __init__(self, numero, titular, saldo, limite):
        ##Dois underscore a frente do atributo significa que ele é um atributo privado
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Seu saldo atual é R$ {}.".format(self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Valor superior ao limite disponível atualmente.")

    def tranfere(self, valor, conta_destino):
        self.saca(valor)
        conta_destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular.capitalize()

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    def __pode_sacar(self, valor):
        return valor <= self.__saldo + self.__limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigo_banco_list():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}