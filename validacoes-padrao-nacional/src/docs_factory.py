from cpf_cnpj_utils import CpfUtils, CnpjUtils


class DocFactory:

    @staticmethod
    def gerar_documento(documento):
        if DocFactory.is_cpf(documento):
            return CpfUtils(documento)
        elif DocFactory.is_cnpj(documento):
            return CnpjUtils(documento)
        else:
            print("Quantidade de dígitos inválida!")

    def is_cpf(self):
        return len(self) == 11

    def is_cnpj(self):
        return len(self) == 14
