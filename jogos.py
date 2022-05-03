import forca
import advinhacao

print("================================")
print("=======Escolha o seu jogo=======")
print("================================")

print("1 - Forca")
print("2 - Advinhação")

jogo = int(input("Qual o jogo? "))

if jogo == 1:
    print("Iniciando forca")
    forca.jogar()
elif jogo == 2:
    print("Iniciando advinhação")
    advinhacao.jogar()