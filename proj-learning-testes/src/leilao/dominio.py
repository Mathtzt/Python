import sys
from copy import deepcopy


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def fazer_lance(self, leilao, valor):
        if valor > self.__carteira:
            raise ValueError("Valor superior ao disponível na carteira!")

        lance_do_apostador = Lance(self, valor)
        leilao.realizar_lance(lance_do_apostador)

    def debita_carteira(self, valor):
        self.__carteira -= valor

    def deposita_carteira(self, valor):
        self.__carteira += valor


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []

        self.maior_lance = sys.float_info.min  # menor valor que o float pode ter no sistema
        self.menor_lance = sys.float_info.max  # maior valor que o float pode ter no sistema

    @property
    def lances(self):
        # return self.__lances[:] ##colocando o [:] estamos devolvendo uma cópia rasa da lista em questão
        return deepcopy(self.__lances)  # dessa forma estamos criando um cópia profunda da lista em questão

    def realizar_lance(self, lance):
        if not self.__lances or \
                (self.__lances[-1].usuario.nome != lance.usuario.nome and self.__lances[-1].valor < lance.valor):  # index -1, busca o ultimo item da lista

            self.__lances.append(lance)
            lance.usuario.debita_carteira(lance.valor)

            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor
        else:
            raise ValueError("O mesmo usuário não pode propor dois lances seguidos e o lance não pode ser inferior ao ultimo lance realizado")