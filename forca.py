def jogar():
    print("================================")
    print("Bem-vindo ao jogo de forca!")
    print("================================")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip()

        i = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                print("A letra {} está na posição {}".format(letra, i))
            i = i + 1


    print("Fim do jogo.")



if(__name__ == "__main__"):
    jogar()