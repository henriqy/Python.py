print("********************************")
print("bem vindo ao jogo de adivinhacao")
print("********************************")

numero_secreto = 42

chute_str = input("Digite o seu numero: ")

chute = int(chute_str)

if(numero_secreto == chute):
    print("voce acertou")
else:
    print("voce errou")
    