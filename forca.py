def jogar_forca():
    print("********************************")
    print("Bem vindo ao jogo de advinhação!")
    print("********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    #enquanto não enforcou E o jogador não acertou (true and true) = true
    #and é um operador lógico

    while (not enforcou and not acertou):

        chute = input("Qual letra? {} : ".format(letras_acertadas))

    #strip e lower

        chute_lower_strip = chute.lower().strip()

        index = 0
        for letra in palavra_secreta:
            if(chute_lower_strip == letra.lower()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)
        letras_faltando = str(letras_acertadas.count('_'))
        print('Ainda faltam acertar {} letras'.format(letras_faltando))

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar_forca()

