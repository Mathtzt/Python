##Esse snippet analisa a frequencia de letras em um texto
#Por default retorna as 10 mais comuns
from collections import Counter

def analisa_frequencia_letras(texto, rank = 10):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(rank)
    for caractere, proporcao in mais_comuns:
        print("Caractere: {} => {:.2f}%".format(caractere, proporcao * 100))
