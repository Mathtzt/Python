class CpfUtils:

    def __init__(self, documento):
        if self.cpf_validator(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido.")

    def __str__(self):
        return self.cpf_format()

    def cpf_validator(self, documento):
        return True if len(documento) else False

    def cpf_format(self):
        return "{}.{}.{}-{}".format(self.cpf[0:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:11])