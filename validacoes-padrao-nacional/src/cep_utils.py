"""
Classe realizará a validação de um CEP através da API do VIACEP,
buscando informações a respeito do endereço do respectivo CEP
"""
import requests


class CEPUtils:

    def __init__(self, cep):
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def __str__(self):
        return self.format_cep(self.cep)

    def cep_e_valido(self, cep):
        return True if len(cep) == 8 else False

    def format_cep(self, cep):
        return "{}-{}".format(cep[0:5], cep[5:8])

    @staticmethod
    def get_dados_from_cep(cep):
        BASE_URL = f"https://viacep.com.br/ws/{cep}/json/"
        r = requests.get(BASE_URL)
        return r.json()
