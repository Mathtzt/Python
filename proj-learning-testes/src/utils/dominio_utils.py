from src.leilao.dominio import Usuario, Lance, Leilao


class DominioUtils:

    @staticmethod
    def gera_lances_leilao():
        math = Usuario("Math")
        ana = Usuario("Ana")
        joao = Usuario("Joao")

        lance_da_ana = Lance(ana, 100)
        lance_do_math = Lance(math, 200)
        lance_do_joao = Lance(joao, 150)

        leilao = Leilao('Churrasqueira')
        leilao.lances.append(lance_da_ana)
        leilao.lances.append(lance_do_math)
        leilao.lances.append(lance_do_joao)
        return leilao

    @staticmethod
    def gera_lance_unico_leilao():
        fabio = Usuario("Fabio")
        lance_do_fabio = Lance(fabio, 150)

        leilao = Leilao('Celular')
        leilao.lances.append(lance_do_fabio)

        return leilao

