import random

def jogar():

    print("********************************")
    print("bem vindo ao jogo de adivinhacao")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tetantivas = 3
    rodada = 1
    pontos = 1000


    print("Choose the level difficult")
    print("(1) Easy (2) Medium (3)Hard (4) God")
    print("\n")
    level = int(input("Type the difficult: "))

    if(level == 1):
        total_de_tetantivas = 20

    elif(level == 2):
        total_de_tetantivas = 10

    elif(level == 3):
        total_de_tetantivas = 5

    elif(level == 4):
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
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

        if(numero_secreto == chute):
            print("\n")
            print("voce acertou e fez {} pontos".format(pontos))
            print("\n")
            print("Fim do Jogo")
            print("\n")
            print("       ___________      \n")
            print("      '._==_==_=_.'     \n")
            print("      .-\\:      /-.    \n")
            print("     | (|:.     |) |    \n")
            print("      '-|:.     |-'     \n")
            print("        \\::.    /      \n")
            print("         '::. .'        \n")
            print("           ) (          \n")
            print("         _.' '._        \n")
            print("        '-------'       \n\n")
            break
        else:
            if(maior):
                print("voce errou, o seu chute foi maior que o numero secreto")

            elif(menor):
                print("Voce errou, seu chute foi menor que o numero secreto")
        
        if(rodada >= total_de_tetantivas):
            print("\n")
            print("Quantidade de pontos: {}".format(pontos))
            print("Fim do Jogo")
            print("\n")

            print("    _______________         \n")
            print("   /               \\       \n") 
            print("  /                 \\      \n")
            print("//                   \\/\\  \n")
            print("\\|   XXXX     XXXX   | /   \n")
            print(" |   XXXX     XXXX   |/     \n")
            print(" |   XXX       XXX   |      \n")
            print(" |                   |      \n")
            print(" \\__      XXX      __/     \n")
            print("   |\\     XXX     /|       \n")
            print("   | |           | |        \n")
            print("   | I I I I I I I |        \n")
            print("   |  I I I I I I  |        \n")
            print("   \\_             _/       \n")
            print("     \\_         _/         \n")
            print("       \\_______/           \n")
        rodada = rodada + 1
        

        