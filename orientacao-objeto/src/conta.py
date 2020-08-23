class Conta:
    ##construtor no python... manter o parametro self inserido pelo python que significa o endereço de memória que será gravado o objeto criado
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Seu saldo atual é R$ {}.".format(self.saldo))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor
