import random

def jogar():
    mensagem_abertura()
    ##variaveis
    enforcou = False
    acertou = False
    max_tentativas = 7
    ##
    palavra_secreta = inicializa_palavra_from_arquivo()

    letras_acertadas = ["_" for letra in palavra_secreta] ##printa traços da quantidade de letras da palavra secreta
    print('A palavra é: ')
    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ").strip().upper()

        max_tentativas = verifica_se_acertou(chute, letras_acertadas, max_tentativas, palavra_secreta)
        enforcou = max_tentativas == 0
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

## Funções auxiliares -------------------------------------------
def verifica_se_acertou(chute, letras_acertadas, max_tentativas, palavra_secreta):
    if (chute in palavra_secreta):
        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                letras_acertadas[index] = letra
            index += 1
    else:
        max_tentativas -= 1
        desenha_forca(max_tentativas)
    return max_tentativas


def inicializa_palavra_from_arquivo():
    with open('palavras-frutas-forca.txt', 'r') as arquivo_palavras:
        palavras = []
        for palavra in arquivo_palavras:
            palavra = palavra.strip().upper()
            palavras.append(palavra)
        palavra_secreta = palavras[random.randrange(0, len(palavras))]
    return palavra_secreta


def mensagem_abertura():
    print("*********************************")
    print("** Bem vindo ao jogo da Forca! **")
    print("*********************************\n")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
#####################################################
if (__name__ == "__main__"):
    jogar()