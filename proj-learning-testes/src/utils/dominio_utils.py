from src.leilao.dominio import Usuario, Lance, Leilao


class DominioUtils:

    @staticmethod
    def gera_lances_leilao():
        math = Usuario("Math")
        ana = Usuario("Ana")
        joao = Usuario("Joao")

        lance_da_ana = Lance(ana, 100)
        lance_do_joao = Lance(joao, 150)
        lance_do_math = Lance(math, 200)

        leilao = Leilao('Churrasqueira')
        leilao.realizar_lance(lance_da_ana)
        leilao.realizar_lance(lance_do_joao)
        leilao.realizar_lance(lance_do_math)
        return leilao

    @staticmethod
    def gera_lance_unico_leilao(leilao=None, nome_apostador="Fabio", valor=150):
        nome = Usuario(nome_apostador)
        lance_do_apostador = Lance(nome, valor)

        if leilao is None:
            leilao = Leilao('Celular')
            leilao.realizar_lance(lance_do_apostador)
        else:
            leilao.realizar_lance(lance_do_apostador)

        return leilao
