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
        if self._eh_valor_valido(valor):
            raise ValueError("Valor superior ao disponível na carteira!")

        lance_do_apostador = Lance(self, valor)
        leilao.realizar_lance(lance_do_apostador)

    def debita_carteira(self, valor):
        self.__carteira -= valor

    def deposita_carteira(self, valor):
        self.__carteira += valor

    def _eh_valor_valido(self, valor):
        return valor > self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        """
        Utilização da biblioteca sys:
        -> sys.float_info.min  retornaria menor valor que o float pode ter no sistema 
        -> sys.float_info.max  retornaria maior valor que o float pode ter no sistema
        """
        self.menor_lance = 0
        self.maior_lance = 0

    @property
    def lances(self):
        # return self.__lances[:] ##colocando o [:] estamos devolvendo uma cópia rasa da lista em questão
        return deepcopy(self.__lances)  # dessa forma estamos criando um cópia profunda da lista em questão

    def realizar_lance(self, lance):
        if self._eh_lance_valido(lance):
            if self._lances_vazios():
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor

            self.__lances.append(lance)
            lance.usuario.debita_carteira(lance.valor)
        else:
            raise ValueError(
                "O mesmo usuário não pode propor dois lances seguidos e o lance não pode ser inferior ao ultimo lance realizado")

    def _lances_vazios(self):
        return not self.__lances

    def _usuario_diferente_do_ultimo_lance(self, lance):
        return self.__lances[-1].usuario.nome != lance.usuario.nome  # index -1, busca o ultimo item da lista

    def _valor_superior_ao_ultimo_lance(self, lance):
        return self.__lances[-1].valor < lance.valor

    def _eh_lance_valido(self, lance):
        return self._lances_vazios() or \
               (self._usuario_diferente_do_ultimo_lance(lance) and
                self._valor_superior_ao_ultimo_lance(lance))
