from src.utils.dominio_utils import DominioUtils

leilao = DominioUtils.gera_lances_leilao()

print("\nTeste 1")
for lance in leilao.lances:
    print(f"O usuário {lance.usuario.nome} deu um lance de {lance.valor}")

print("\nTeste 2")
print(f"O menor lance foi de {leilao.menor_lance}, já o maior foi de {leilao.maior_lance}")
