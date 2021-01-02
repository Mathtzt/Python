from src.leilao.dominio import Usuario, Leilao, Lance, Avaliador
from src.utils.dominio_utils import DominioUtils

leilao = DominioUtils.gera_lances_leilao()

print("\nTeste 1")
for lance in leilao.lances:
    print(f"O usuário {lance.usuario.nome} deu um lance de {lance.valor}")

print("\nTeste 2")
avaliador = Avaliador()
avaliador.avalia(leilao)
print(f"O menor lance foi de {avaliador.menor_lance}, já o maior foi de {avaliador.maior_lance}")