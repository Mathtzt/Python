from unittest import TestCase

from src.leilao.dominio import Avaliador
from src.utils.dominio_utils import DominioUtils


class TestAvaliador(TestCase):
    def test_avalia(self):
        leilao = DominioUtils.gera_lances_leilao()

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100

        self.assertEqual(
            menor_valor_esperado,
            avaliador.menor_lance
        )
