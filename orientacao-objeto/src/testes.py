from src.heranca_multipla import Tutor, Professor

"""
Método definido para realização dos testes da aplicação, como solicitados.
"""
def tests():
    print("** Testes da aplicação")

    jose = Tutor('José', 40) ## Instanciando o objeto do tipo Tutor, passando o nome e idade como parâmetros.
    fabio = Professor('Fábio', 51) ## Instanciando o objeto do tipo Professor, passando o nome e idade como parâmetros.
    print("\nTESTE 1 ============")
    print(f"A idade do josé é: {jose.idade}")
    print("\nTESTE 2 ============")
    jose.registra_horas(12)
    print("\nTESTE 3 ============")
    jose.mostrar_tarefas()
    print("\nTESTE 4 ============")
    jose.buscar_lista_atendimentos()
    print("\nTESTE 5 ============") ##testar se mixin está correto
    print(jose)

    print("\nTESTE 6 ============") ##testando polimorfismo
    fabio.mostrar_tarefas()
    print("\nTESTE 7 ============") ##testando método próprio do professor
    fabio.buscar_turmas_do_mes('fevereiro')
"""
Quando rodamos diretamente um arquivo no Python, ele internamente cria uma variável e a preenche.
Essa variável é a __name__, e ela é preenchida com o valor __main__ caso o arquivo seja executado diretamente. Vamos então fazer if para verificar se ela está preenchida ou não para assim rodar os tests, assegurando que o programa executará corretamente independentemente de como ele for executado:
"""
if (__name__ == "__main__"): ## Os parenteses são opcionais. Eu decidi por os colocar.
    tests() ## Chamando método que rodará os testes da nossa aplicação.