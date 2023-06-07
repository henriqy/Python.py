print("********************************")
print("bem vindo ao jogo de adivinhacao")
print("********************************")

numero_secreto = 42
total_de_tetantivas = 3
rodada = 1

for rodada in range (1,total_de_tetantivas + 1):
    print("tentativa {} de {}".format( rodada, total_de_tetantivas))

    chute_str = input("Digite o seu numero: ")

    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Nao pode chutar numeros menores que 1 ou maiores que 100")
        continue

    acertou = (numero_secreto == chute)
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(numero_secreto == chute):
        print("voce acertou")
        break
    else:
        if(maior):
            print("voce errou, o seu chute foi maior que o numero secreto")

        elif(menor):
            print("Voce errou, seu chute foi menor que o numero secreto")
    
    rodada = rodada + 1
    
    print("Fim do Jogo")
    