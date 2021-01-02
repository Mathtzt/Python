from unittest import TestCase

from src.leilao.dominio import Avaliador
from src.utils.dominio_utils import DominioUtils


class TestAvaliador(TestCase):
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
