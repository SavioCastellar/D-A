import random

def jogar():
    print("================================")
    print("Bem-vindo ao jogo de forca!")
    print("================================")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            i = 0
            for letra in palavra_secreta:
                if chute.upper() == letra.upper():
                    letras_acertadas[i] = letra
                i += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você venceu!")
    else:
        print("Você perdeu.")
    print("Fim do jogo.")

if(__name__ == "__main__"):
    jogar()