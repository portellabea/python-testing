import random

def jogar_adivinhacao():

    print("********************************")
    print("Bem vindo ao jogo de advinhação!")
    print("********************************")

    numero_secreto = round(random.random() * 100)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #enquanto ainda há tentativas disponíveis: execute o código abaixo.
    #em cada laço será subtraido um do total de tentativas.

    for rodada in range(1, total_de_tentativas + 1):
        #saberemos a rodada atual
        print("Tentativas {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite o seu número: "))
        print("Você digitou", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100. Você perdeu uma rodada!")
            continue

        acertou = numero_secreto == chute
        chute_foi_maior = chute > numero_secreto
        chute_foi_menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(chute_foi_maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif(chute_foi_menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
        pontos_perdidos = abs(round(random.random() * 100) - chute)
        pontos = pontos - pontos_perdidos
        rodada = rodada + 1

    print("Fim do jogo!")


