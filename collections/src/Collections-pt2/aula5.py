###Testando uso de diversas coleções
##Textos aleatórios buscados na internet
from collections import Counter
from snippet import analisa_frequencia_letras

texto1 = """
    Empresas que participaram de um pregão do Ministério da Saúde garantiram o fornecimento de apenas 2,4% do total de seringas e agulhas que o governo tentou comprar para serem usadas na vacinação contra a Covid-19.
    
    A informação foi divulgada pelo jornal "O Estado de S. Paulo" e confirmada pela TV Globo. O pregão, realizado na terça (29), previa a compra de um total de 331 milhões de seringas, mas as empresas que participaram ofertaram 7,9 milhões.

Empresas que participaram do pregão eletrônico reclamaram que o edital encomendava seringas e agulhas como um só produto, e que os preços estavam abaixo dos praticados

Também na terça, o secretário-executivo do Ministério da Saúde, Élcio Franco, informou que o Brasil deverá começar a vacinação entre 20 de janeiro e 10 de fevereiro de 2021, mas que precisa que "os fabricantes obtenham o registro [das vacinas da Covid-19] junto à Anvisa".
"""

texto2 = """
    A pandemia escancara quantos países há dentro do Brasil e como inexiste o senso de coletividade. Enquanto a crise sanitária começava sua violenta trajetória, o futebol ignorava a escalada de mortes e costurava sua própria bolha de privilegiados, desprezando a calamidade instalada na sociedade para retomar a roda da fortuna. Dessa forma, é apenas maligno reflexo que seus protagonistas sintam-se à vontade para ignorar a realidade -- ou, mais decepcionante ainda, para negar a realidade.

A festa de Ano Novo organizada por Neymar em uma mansão em Mangaratiba, no Rio de Janeiro, é nada mais do que isso: uma atitude ególatra de alguém completamente alheio aos problemas da sociedade. A terrível situação sanitária concede contornos sinistros ao capricho narcisista, mas está longe de causar surpresa, pois ignorar as agruras sociais do país de origem é o modo de vida da grande maioria dos craques superfaturados.

Neymar é uma pessoa pública cujas atitudes influenciam milhares de pessoas. Algo que, aos 28 anos, ele não percebe ou faz questão de ignorar. Ao promover uma festa de dantescas proporções, redoma de diversão propositalmente blindada do fúnebre entorno que hoje é o Brasil, o jogador desautoriza todas as medidas sanitárias e contribui para que a tragédia se alastre -- de forma indireta, pela mensagem de desprezo à pandemia, e também na prática, pois é responsável por colocar em risco não apenas os convidados, mas todos que convivem com eles, além dos trabalhadores que estão expostos a um evento onde a aglomeração é a regra. Através de uma extravagância individual vemos a completa ausência do senso de responsabilidade coletiva.
"""

###Contando a quantidade de letras no texto 1
print("Teste 1")
aparicoes = Counter(texto1.lower())
print(aparicoes)

###Quantidade total de caracteres no texto 1
print("\nTeste 2")
total_de_caracteres = sum(aparicoes.values())
print("Total de caracteres: {}".format(total_de_caracteres))

###Frequencia de aparição de cada letra
print("\nTeste 3")
for letra, frequencia in aparicoes.items():
    tupla = (letra, frequencia / total_de_caracteres)
    print(tupla)

##Buscando as 10 aparições mais comuns
print("\nTeste 4")
proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
proporcoes = Counter(dict(proporcoes))
mais_comuns = proporcoes.most_common(10)
print(mais_comuns)

##teste
print("\nTeste 5")
analisa_frequencia_letras(texto2)