"""
Projeto criado para gerenciar validações de:
    1. CPF
    2. CNPJ
    3. Telefone
    4. Data/hora
Toda implementação é de caráter de estudo.
"""
from cpfUtils import CpfUtils
from validate_docbr import CPF

cpf_usuario = "01234567890"
objeto_cpf = CpfUtils(cpf_usuario)
print(objeto_cpf)

cpf = CPF()
cpf.validate(cpf_usuario)

