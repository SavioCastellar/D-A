import random


def jogar():
    mensagem_abertura()
    palavra_secreta = gera_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = solicita_chute()

        if chute in palavra_secreta:
            verifica_chute(palavra_secreta, letras_acertadas, chute)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

def mensagem_abertura():
    print("================================")
    print("Bem-vindo ao jogo de forca!")
    print("================================")

def gera_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def solicita_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def verifica_chute(palavra_secreta, letras_acertadas, chute):
    i = 0
    for letra in palavra_secreta:
        if chute.upper() == letra.upper():
            letras_acertadas[i] = letra
        i += 1

def imprime_mensagem_vencedor():
    print("Você venceu!")

def imprime_mensagem_perdedor():
    print("Você perdeu!")

if(__name__ == "__main__"):
    jogar()