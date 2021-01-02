from src.leilao.dominio import Usuario, Lance, Leilao


class DominioUtils:

    @staticmethod
    def gera_lances_leilao():
        math = Usuario("Math")
        ana = Usuario("Ana")

        lance_da_ana = Lance(ana, 100)
        lance_do_math = Lance(math, 200)

        leilao = Leilao('Churrasqueira')
        leilao.lances.append(lance_da_ana)
        leilao.lances.append(lance_do_math)
        return leilao
