import adivinhacao
import forca

print("*********************************")
print("** Bem vindo ao menu de jogos! **")
print("*********************************")

print("\nEscolha qual dos nossos jogos deseja jogar:")
print("1 - Adivinhação\n2 - Forca")
opcao = int(input("R: "))

if (opcao == 1):
    adivinhacao.jogar()
elif (opcao == 2):
    forca.jogar()
else:
    print("\nOpção inválida!")