from unittest import TestCase
from src.utils.dominio_utils import DominioUtils


class TestLeilao(TestCase):
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

    O tipo de teste que garante que algo que já funcionava continue funcionando,
    não importando as funcionalidades, é chamado de Testes de regressão no mercado.
    """

    def test_deve_retornar_menor_e_maior_valor_leilao(self):
        leilao = DominioUtils.gera_lances_leilao()

        menor_valor_esperado = 100
        maior_valor_esperado = 200

        self.assertEqual(
            menor_valor_esperado,
            leilao.menor_lance
        )
        self.assertEqual(
            maior_valor_esperado,
            leilao.maior_lance
        )

    def test_deve_retornar_valores_iguais_quando_lance_unico(self):
        leilao = DominioUtils.gera_lance_unico_leilao()

        valor_lance_unico = 150

        self.assertEqual(
            valor_lance_unico,
            leilao.menor_lance
        )
        self.assertEqual(
            valor_lance_unico,
            leilao.maior_lance
        )

    def test_deve_permitir_fazer_lance_quando_leilao_nao_tiver_lances(self):
        leilao = DominioUtils.gera_lance_unico_leilao()

        quantidade_de_lances_ja_realizados = len(leilao.lances)

        self.assertEqual(
            1,
            quantidade_de_lances_ja_realizados
        )

    def test_deve_permitir_fazer_lance_quando_ultimo_apostador_seja_diferente(self):
        leilao = DominioUtils.gera_lance_unico_leilao()
        leilao = DominioUtils.gera_lance_unico_leilao(leilao, "João", 225)

        quantidade_lances_recebidos = len(leilao.lances)

        self.assertEqual(
            2,
            quantidade_lances_recebidos
        )

    def test_nao_deve_permitir_fazer_lance_consecutivo_por_mesmo_apostador(self):
        with self.assertRaises(ValueError):  # teste para verificar se a exceção realmente está sendo lançada
            leilao = DominioUtils.gera_lance_unico_leilao()
            DominioUtils.gera_lance_unico_leilao(leilao)

    def teste_nao_deve_permitir_fazer_lance_com_valor_inferior_ao_ultimo_lance(self):
        with self.assertRaises(ValueError):
            leilao = DominioUtils.gera_lance_unico_leilao()
            DominioUtils.gera_lance_unico_leilao(leilao, "Carla", 60)
