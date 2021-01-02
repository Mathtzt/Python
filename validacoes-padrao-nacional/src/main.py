"""
Projeto criado para gerenciar validações de:
    1. CPF
    2. CNPJ
    3. Email
    4. Telefone
    5. Data/hora
    6. API CEP
Toda implementação é de caráter de estudo.
"""
from docs_factory import DocFactory
from utils import EmailUtils, TelefoneUtils, DateTimeUtils
from cep_utils import CEPUtils

print("\nTeste 1")
cpf_teste = "01234567891"
DocFactory.gerar_documento(cpf_teste)

print("\nTeste 2")
cnpj_teste = "00000000000191"
cnpj = DocFactory.gerar_documento(cnpj_teste)
print(cnpj)

print("\nTeste 3")
email = "teste@email.com"
print(EmailUtils.valida_email(email))

print("\nTeste 4")
telefone_sem_ddd = "12344567"
print(TelefoneUtils.format_telefone_sem_ddd(telefone_sem_ddd))

celular_sem_ddd = "912344567"
print(TelefoneUtils.format_telefone_sem_ddd(celular_sem_ddd))

telefone_com_ddd = "2112344567"
print(TelefoneUtils.format_telefone_com_ddd(telefone_com_ddd))

celular_com_ddd = "21912344567"
print(TelefoneUtils.format_telefone_com_ddd(celular_com_ddd))

print("\nTeste 5")
data_cadastro = DateTimeUtils.get_momento_cadastro()
mes_cadastro = DateTimeUtils.get_mes_cadastro(data_cadastro)
dia_semana_cadastro = DateTimeUtils.get_dia_semana_cadastro(data_cadastro)
print(data_cadastro)
print(mes_cadastro)
print(dia_semana_cadastro)
print(DateTimeUtils.get_momento_cadastro_formatado(data_cadastro))

print("\nTeste 6")
cep = "01001000"
print(CEPUtils(cep))

print("\nTeste 7")
json_cep = CEPUtils.get_dados_from_cep(cep)
print(json_cep)

print("\nTeste 8")
print(f"{json_cep['logradouro']}, {json_cep['localidade']} - {json_cep['uf']}")