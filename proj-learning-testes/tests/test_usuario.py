"""
Classe para utilização do Pytest
Com a biblio instalada, rodar pytest no terminal
Ele buscara os métodos dentro da pasta test e os métodos com a nomeclatura test_* ou *_test
"""
from src.leilao.dominio import Usuario, Leilao
import pytest


@pytest.fixture
def stp_usuario():
    return Usuario("Math", 1000)


@pytest.fixture
def stp_leilao():
    return Leilao("Carro")


def test_deve_subtrair_valor_da_carteira_usuario_quando_fazer_lance(stp_usuario, stp_leilao):
    stp_usuario.fazer_lance(stp_leilao, 200)
    assert stp_usuario.carteira == 800


def test_deve_permitir_fazer_lance_quando_o_valor_for_menor_ou_igual_valor_carteira(stp_usuario, stp_leilao):
    stp_usuario.fazer_lance(stp_leilao, 200)
    assert stp_usuario.carteira == 800


def test_nao_deve_permitir_fazer_lance_quando_o_valor_for_superior_valor_carteira(stp_usuario, stp_leilao):
    with pytest.raises(ValueError):
        stp_usuario.fazer_lance(stp_leilao, 1500)
