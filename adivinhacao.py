import random

print("********************************")
print("bem vindo ao jogo de adivinhacao")
print("********************************")

numero_secreto = random.randrange(1,101)
total_de_tetantivas = 3
rodada = 1

print("Choose the level difficult")
print("(1) Easy (2) Medium (3)Hard (4) God")

level = int(input("Type the difficult: "))

if(level == 1):
    total_de_tetantivas = 20

elif(level == 2):
    total_de_tetantivas = 10

elif(level == 3):
    total_de_tetantivas = 5

else:
    total_de_tetantivas = 1

for rodada in range (1,total_de_tetantivas + 1):
    print()
    print("tentativa {} de {}".format( rodada, total_de_tetantivas))
    print()
    chute_str = input("Digite um numero entre 1 e 100: ")

    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Nao pode chutar numeros menores que 1 ou maiores que 100")
        continue

    acertou = (numero_secreto == chute)
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(numero_secreto == chute):
        print("voce acertou")
        print()
        print("Fim do Jogo")
        break
    else:
        if(maior):
            print("voce errou, o seu chute foi maior que o numero secreto")

        elif(menor):
            print("Voce errou, seu chute foi menor que o numero secreto")
    
    rodada = rodada + 1
    
print("Fim do Jogo")
    