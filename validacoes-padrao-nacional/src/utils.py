import re
from datetime import datetime, timedelta


class RegexUtils:
    emailPattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    telefonePattern = '([0-9]{2})?([0-9]{4,5})([0-9]{4})'


class EmailUtils:

    @staticmethod
    def valida_email(email):
        if re.search(RegexUtils.emailPattern, email):
            return True
        else:
            return False


class TelefoneUtils:

    @staticmethod
    def valida_telefone(telefone):
        if re.search(RegexUtils.telefonePattern, telefone):
            return True
        else:
            return False

    @staticmethod
    def format_telefone_sem_ddd(telefone):
        resposta = re.search(RegexUtils.telefonePattern, telefone)
        return "{}-{}".format(resposta.group(2), resposta.group(3))

    @staticmethod
    def format_telefone_com_ddd(telefone):
        resposta = re.search(RegexUtils.telefonePattern, telefone)
        return "({}) {}-{}".format(resposta.group(1), resposta.group(2), resposta.group(3))


class DateTimeUtils:

    @staticmethod
    def get_momento_cadastro():
        return datetime.today()

    @staticmethod
    def get_momento_cadastro_formatado(self):
        return DateTimeUtils.format_data_hora(self)

    @staticmethod
    def get_mes_cadastro(self):
        return DateTimeUtils.get_meses_ano_formatado(self.month-1)

    @staticmethod
    def get_dia_semana_cadastro(self):
        return DateTimeUtils.get_dia_semana_formatado(self.weekday())

    @staticmethod
    def get_meses_ano_formatado(self):
        meses_do_ano = [
            "janeiro",
            "fevereiro",
            "março",
            "abril",
            "maio",
            "junho",
            "julho",
            "agosto",
            "setembro",
            "outubro",
            "novembro",
            "dezembro"
        ]
        return meses_do_ano[self]

    @staticmethod
    def get_dia_semana_formatado(self):
        dias_da_semana = [
            "domingo"
            "segunda-feira",
            "terça-feira",
            "quarta-feira",
            "quinta-feira",
            "sexta-feira",
            "sabado"
        ]
        return dias_da_semana[self]

    @staticmethod
    def format_data_hora(self):
        return self.strftime("%d/%m/%Y - %H:%M")
