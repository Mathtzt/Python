from unittest import TestCase

from src.leilao.dominio import Avaliador
from src.utils.dominio_utils import DominioUtils


class TestAvaliador(TestCase):
    """
    Outras dicas/métodos importantes da classe TestCase:
    -> setUp: executa o trecho de código antes de cada método de testes
    -> tearDown: executa o trecho de código logo após a execução de cada teste
    -> setUpClass: executa o trecho de código no momento que a classe é criada
    -> tearDownClass: executa o trecho de código após o último teste da classe ser rodado

    Obs: Os métodos tearDown e tearDownClass são muito utilizados em testes que
    integram duas partes do sistema - banco de dados, sistemas externos,
    ou então desejamos fechar uma conexão que foi aberta.

    Tais tipos de testes, que verificam como duas partes do sistema se integram,
    são chamados de testes de integração.
    """

    def test_deve_retornar_menor_e_maior_valor_leilao(self):
        leilao = DominioUtils.gera_lances_leilao()

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100
        maior_valor_esperado = 200

        self.assertEqual(
            menor_valor_esperado,
            avaliador.menor_lance
        )
        self.assertEqual(
            maior_valor_esperado,
            avaliador.maior_lance
        )

    def test_deve_retornar_valores_iguais_quando_lance_unico(self):
        leilao = DominioUtils.gera_lance_unico_leilao()

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        valor_lance_unico = 150

        self.assertEqual(
            valor_lance_unico,
            avaliador.menor_lance
        )
        self.assertEqual(
            valor_lance_unico,
            avaliador.maior_lance
        )
