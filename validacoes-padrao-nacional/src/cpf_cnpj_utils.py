from validate_docbr import CPF, CNPJ


class CpfUtils:
    def __init__(self, documento):
        if self.cpf_validator(documento):
            self.cpf_ou_cnpj = documento
        else:
            print("Cpf inválido!!")

    def __str__(self):
        return self.cpf_format()

    def cpf_format(self):
        return "{}.{}.{}-{}".format(self.cpf_ou_cnpj[0:3], self.cpf_ou_cnpj[3:6], self.cpf_ou_cnpj[6:9],
                                    self.cpf_ou_cnpj[9:11])

    def cpf_validator(self, cpf_base):
        valida_cpf = CPF()
        return valida_cpf.validate(cpf_base)


class CnpjUtils:

    def __init__(self, documento):
        if self.cnpj_validator(documento):
            self.cpf_ou_cnpj = documento
        else:
            print("Cnpj inválido!!")

    def __str__(self):
        return self.cnpj_format()

    def cnpj_format(self):
        return "{}.{}.{}/{}-{}".format(self.cpf_ou_cnpj[0:2], self.cpf_ou_cnpj[2:5], self.cpf_ou_cnpj[5:8],
                                       self.cpf_ou_cnpj[8:12], self.cpf_ou_cnpj[12:14])

    def cnpj_validator(self, cnpj_base):
        valida_cnpj = CNPJ()
        return valida_cnpj.validate(cnpj_base)

