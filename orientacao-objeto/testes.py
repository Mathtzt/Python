from conta import Conta
from datas import Data


def test_class_conta():
    print("Testando classe conta...")
    conta = Conta(3512, "Exemplo", 500.0, 1500.0)
    conta.extrato()
    conta.deposita(150.0)
    conta.extrato()


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
