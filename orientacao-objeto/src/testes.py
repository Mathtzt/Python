from src.conta import Conta
from src.datas import Data

def test_class_conta():
    print("Testando classe conta...")
    conta = Conta(3512, "Exemplo", 500.0, 1500.0)
    conta2 = Conta(1412, "Exemplo2", 250.0, 1500.0)
    conta.extrato()
    conta.deposita(150.0)
    conta.extrato()
    conta.tranfere(250, conta2)
    conta.extrato()
    conta2.extrato()
    conta.saca(2000)
    print(Conta.codigo_banco())
    print(Conta.codigo_banco_list())

def test_class_data():
    print("Testando classe data...")
    data = Data(12, 5, 2020)
    data.format()


###
if (__name__ == "__main__"):
    print()
    test_class_conta()
    print()
    test_class_data()
