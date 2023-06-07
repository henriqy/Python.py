print("********************************")
print("bem vindo ao jogo de adivinhacao")
print("********************************")

numero_secreto = 42
total_de_tetantivas = 3
rodada = 1

while(rodada <= total_de_tetantivas):
    print("tentativa {} de {}".format( rodada, total_de_tetantivas))

    chute_str = input("Digite o seu numero: ")

    chute = int(chute_str)

    acertou = (numero_secreto == chute)
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(numero_secreto == chute):
        print("voce acertou")
    else:
        if(maior):
            print("voce errou, o seu chute foi maior que o numero secreto")

        elif(menor):
            print("Voce errou, seu chute foi menor que o numero secreto")
        
    print("Fim do Jogo")
    
    rodada = rodada + 1