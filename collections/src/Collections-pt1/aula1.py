##Esse arquivo foi criado para o estudo das Coleções no python em especial as listas e tuplas.

##Criando lista simples
##Podemos dizer que é uma sequencia de acesso aleatório, como um array
idades = [39, 15, 42, 88]
print(type(idades))

print(len(idades)) # tamanho da lista
print(idades[0]) # acessando elemento na pos 0
print(idades) # mostrando lista completa

#No python as listas podem ter seus valores alterados
idades.append(23) # o append insere um valor no fim da lista
print(idades)

print('\nPassando por todos os elementos:')
for idade in idades:
    print(idade)

print('\nRemovendo o elemento 39:')
idades.remove(39) # a função remove, remove (é claro rs) um determinado valor da lista. Caso tenha dois elementos iguais, ele remove o primeiro elemento encontrado na lista.
print(idades)

idades.clear() # remove todos os elementos da lista.
print('\nRemovi todos os elementos da lista')
print(idades)

idades = [39, 15, 42, 88]
print(15 in idades) # um dos modos de descobrir se o valor está contido na lista

print('\nInserindo valor 21 na posição determinada')
idades.insert(0, 21) # o insert, insere na pos 0 o valor 21
print(idades)

## list comprehension exemplos
'''<<<Com o list comprehension é possível aplicar filtros e trasformações>>>'''
print('\nList Comprehension - exemplos')
# Criando uma lista somando idade
idades_ano_que_vem = [(idade + 1) for idade in idades]
print(idades_ano_que_vem)

# Utilizando um condicional na formação tbm
idades_ano_que_vem = [(idade + 1) for idade in idades if idade > 20]
print(idades_ano_que_vem)

## Mutabilidade das listas
'''No exemplo abaixo é possivel perceber que a lista sofreu alterações durante o processamento da função. Isso ocorreu porque a referencia passada para a função ainda existia e permitiu que a alteração ocorresse.'''

print('\nMutabilidade das listas')
def visualizacao(lista):
    print(len(lista))
    lista.append(13)

visualizacao(idades)
print(idades)

'''Esse problema pode ocorrer com parametros com valor default. Para evitar isso o melhor modo é:'''
def test_visualizacao(lista = None):
    if (lista == None):
        lista = list()
        print(len(lista))
        lista.append(13)

print(test_visualizacao())
'''Desse modo, o avaluation do parametro default que só ocorre uma vez garante que a referência mantida não sofra alteração ao chamar a função sem parametro sequencialmente.'''