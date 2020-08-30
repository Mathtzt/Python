from src.conta import Conta
from src.datas import Data
from src.heranca import Programa, Filme, Serie, Playlist
from src.heranca_multipla import Tutor

def test_class_conta():
    print("** Testando classe conta...")
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
    print("** Testando classe data...")
    data = Data(12, 5, 2020)
    data.format()

def test_class_heranca():
    print("** Testando classe herança...")
    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    atlanta = Serie('atlanta', 2018, 2)
    vingadores.dar_likes()
    vingadores.dar_likes()
    vingadores.dar_likes()

    atlanta.dar_likes()
    atlanta.dar_likes()

    programas = [vingadores, atlanta]
    playlist_fds = Playlist('Os melhores', programas)

    for programa in playlist_fds:
        print(programa)

def test_class_heranca_multipla():
    print("** Testando classe herança multipla...")
    jose = Tutor('José')
    jose.registra_horas(12)
    jose.mostrar_tarefas()
    jose.buscar_lista_atendimentos()

    ##testar se mixin está correto
    print(jose)

###
if (__name__ == "__main__"):
    print()
    test_class_conta()
    print()
    test_class_data()
    print()
    test_class_heranca()
    print()
    test_class_heranca_multipla()
