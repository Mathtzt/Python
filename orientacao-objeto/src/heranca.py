##Classe criada para estudar herança e afins
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title() #por convenção utiliza-se um underscore para demonstrar que o atributo é privado, e não ter problemas com o name mangling do python
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    def __str__(self):
        return f'Nome: {self._nome} - Likes: {self._likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.ano} com {self.duracao} min ({self.likes} curtidas)'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.ano} com {self.temporadas} temporadas ({self.likes} curtidas)'
