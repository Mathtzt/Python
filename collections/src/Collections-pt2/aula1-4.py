## Trabalhando com conjuntos (set)
"""Note que um conjunto não suporta indexação e numeros repetidos"""
from collections import defaultdict, Counter

grupoA = {2, 6, 8, 1} #A representação de um conjunto é por meio das {}
grupoB = {6, 1, 10, 5}

##Unindo dois conjuntos
print("\nTeste 1")
print(grupoA | grupoB) #Para a união, utilizamos o caracterer | (pipe - ou)

##Intercessão dois conjuntos
print("\nTeste 2")
print(grupoA & grupoB) #Para a intercessão, utilizamos o caracterer & (e)

##Existe no primeiro grupo e não no segundo
print("\nTeste 3")
print(grupoA - grupoB)

##Ou exclusivo
print("\nTeste 4")
print(grupoA ^ grupoB) #Faz parte do grupo A ou do B mas não dos dois

##Modificando os conjuntos em tempo real
#adicionando elemento. Obs: Note que se o elemento já existir não haverá inclusão de numero repetido
print("\nTeste 5")
grupoA.add(15)
print(grupoA)

##Criando conjunto imutável. Obs: não é possível alterar o conjunto
print("\nTeste 6")
grupoC = frozenset(grupoA)
print(grupoC)

##Conjunto de strings
print("\nTeste 7")
meu_texto = "Bem vindo meu nome é Matheus eu gosto muito de programar e programar é a mesma coisa que me inspira"
meu_conjunto_de_palavras = set(meu_texto.split()) ##split por default quebra as palavras nos espaços em branco
print(meu_conjunto_de_palavras) ##mostrando meu conjunto de palavras

##Criando um dicionário (Possui chave/valor)
print("\nTeste 8")
aparicoes = {
    "Matheus": 1,
    "Bem": 1,
    "é": 2
}
print(type(aparicoes))
print(aparicoes.get("Matheus"))
print(aparicoes.get("onde", 0)) ##colocando valor default para caso não encontre a palavra

#Outras operações com dicionários
print("\nTeste 9")
aparicoes["gosto"] = 2 ##Adicionando novo valor
aparicoes["Matheus"] = 1 ##Alterando valor existente
del aparicoes["Bem"] ##Removendo valor existente
print(aparicoes)

#Iterando pelos items do dicionário
print("\nTeste 10")
for aparicao in aparicoes.items():
    print(aparicao)

#É possível utilizar o list comprehension tranquilamente
print("\nTeste 11")
print(["A palavra é: {}".format(chave) for chave in aparicoes.keys()])

###Desafio
##Contando quantidade de cada palavra em um texto
print("\nTeste 12")
meu_texto = "Bem vindo meu nome é Matheus eu gosto muito de programar e programar é a mesma coisa que me inspira"
meu_texto = meu_texto.lower()
aparicoes = {}
for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1
print(aparicoes)

##Utilizando um dicionário com um valor padrão (defaultdict)
print("\nTeste 13")
aparicoes = defaultdict(int) #bastante utilizando no dia a dia
for palavra in meu_texto.split():
    aparicoes[palavra] += 1 #devido ao defaultdict n precisa passar o valor default explicitamente
print(aparicoes)

#Utilizando o defaultdict para outras classes
print("\nTeste 14")
class Conta:
    def __init__(self):
        print("Criando conta nova")

contas = defaultdict(Conta)
print(contas[10]) #Note que o construtor irá chamar o construtor padrão quando não encontrar o valor

##Utilizando um contador (counter)
print("\nTeste 15")
aparicoes = Counter(meu_texto.split())
print(aparicoes)