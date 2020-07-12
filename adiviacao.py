import random

print("********************************")
print("Bem vindo ao jogo de advinhação!")
print("********************************")

numero_secreto = round(random.random() * 100)
total_de_tentativas = 3

print(numero_secreto)

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
        print("Você acertou!")
        break
    else:
        if(chute_foi_maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif(chute_foi_menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

    rodada = rodada + 1

print("Fim do jogo!")


