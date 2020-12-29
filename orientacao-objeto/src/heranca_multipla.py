"""
A aplicação abaixo foi desenvolvida com intuito de explorar minimamente,
visto que não tem a intenção de alcançar a completude, os conceitos
dos paradigmas abordados pelo Python.
A aplicação ainda explora a herança multipla e polimorfismo/sobrecarga.
"""

## Nesse momento é criado uma classe chamada Funcionário
class Funcionario:
    ## Construtor no python... manter o parametro self inserido pelo python que significa o endereço de memória que será gravado o objeto criado
    ## Definido também como parametros os valores de nome e idade necessários para instaciar um objeto do tipo funcionario
    def __init__(self, nome, idade):
        self.nome = nome ## Atribuição do nome recebido para construção do objeto
        self.__idade = idade ## Atribuição da idade recebida para construção do objeto

    ## Método Getter para acessar o valor do atributo idade do objeto
    @property
    def idade(self):
        return self.__idade

    ## Método Setter para atualizar o valor do atributo idade do objeto com o valor novo recebido por parametro da função
    @idade.setter
    def idade(self, valor):
        self.__idade = valor

    ## Método será comum a todos as classes que extenderem de Funcionário
    def registra_horas(self, horas):
        print(f'Suas {horas} foram registradas')
    ## Método que será sobreescrito pelas classes que extenderem de Funcionário
    def mostrar_tarefas(self):
        print('Você trabalhou muito, resolvendo coisas como: ...')

## Aplicação da Herança Simples. Nesse caso, a classe Professor extende de Funcionario, ou seja, um professor é um tipo de funcionário. Desse modo, ela compartilha dos mesmos atributos de funcionário, isto é, nome e idade.
class Professor(Funcionario):
    ## Método sobreescrito dado a caracteristica mais particular de um professor
    def mostrar_tarefas(self):
        print('Você deu aula de ...')
    ## Método particular de um professor. Definido apenas nessa classe.
    def buscar_turmas_do_mes(self, mes=None):
        print(f'As turmas desse mês de {mes} serão: ...')

## Aplicação da Herança Simples. Nesse caso, a classe Coordenador extende de Funcionario, ou seja, um coordenador é um tipo de funcionário. Desse modo, ela compartilha dos mesmos atributos de funcionário, isto é, nome e idade.
class Coordenador(Funcionario):
    ## Método sobreescrito dado a caracteristica mais particular de um professor
    def mostrar_tarefas(self):
        print('Durante o expediente, realizei: ...')
    ## Método particular de um coordenador. Definido apenas nessa classe.
    def buscar_lista_atendimentos(self):
        print('Todos os atendimentos marcados são: ...')

## Criando um Mixin para exemplo (São apenas classes que podem ser herdadas mas que não dever ser instanciadas, já que servem para disponibilizar comportamentos para outras classes
class Saudacao:
    def __str__(self):
        return f'Caro(a), {self.nome}'

## O Python possui um algoritmo chamado de MRO (Method Resolution Order) que define a ordem para utilização dos métodos quando há herança multipla.
## Definindo uma classe Tutor que extende tanto de professor quanto de coordenador. Assim nesse momento, ocorre uma herança múltipla.
class Tutor(Professor, Coordenador, Saudacao):
    pass