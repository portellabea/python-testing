print("********************************")
print("Bem vindo ao jogo de advinhação!")
print("********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1
#enquanto ainda há tentativas disponíveis: execute o código abaixo.
#em cada laço será subtraido um do total de tentativas.

while(rodada <= total_de_tentativas):
    #saberemos a rodada atual
    print("Tentativas", rodada, "de", total_de_tentativas)
    chute = int(input("Digite o seu número: "))
    print("Você digitou", chute)

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


