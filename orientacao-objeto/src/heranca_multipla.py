class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print(f'Suas {horas} foram registradas')

    def mostrar_tarefas(self):
        print('Você trabalhou muito, resolvendo coisas como: ...')

class Professor(Funcionario):
    def mostrar_tarefas(self):
        print('Você deu aula de ...')

    def buscar_turmas_do_mes(self, mes=None):
        print(f'As turmas desse mês de - {mes} serão: ...')

class Coordenador(Funcionario):
    def mostrar_tarefas(self):
        print('Durante o expediente, realizei: ...')

    def buscar_lista_atendimentos(self):
        print('Todos os atendimentos marcados são: ...')

## Criando um Mixin para exemplo (São apenas classes que podem ser herdadas mas que não dever ser instanciadas, já uqe servem para disponivilizar comportamentos para outras classes
class Saudacao:
    def __str__(self):
        return f'Caro(a), {self.nome}'

## O Python possui um algoritmo chamado de MRO (Method Resolution Order) que define a ordem para utilização dos métodos quando há herança multipla.
class Tutor(Professor, Coordenador, Saudacao):
    pass