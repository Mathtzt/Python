import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 3
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("1 - Fácil\n2 - Médio\n3 - Difícil")
    nivel = int(input("R: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("\tVocê acertou e fez {} pontos!\n".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.\n")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print("Fim do jogo\n")

'''
    Quando rodamos diretamente um arquivo no Python, ele internamente cria uma variável e a preenche.
    Essa variável é a __name__, e ela é preenchida com o valor __main__ caso o arquivo seja executado diretamente. Vamos então fazer if para verificar se ela está preenchida ou não:
'''
if (__name__ == "__main__"):
    jogar()