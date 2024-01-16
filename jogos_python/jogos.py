import forca
import adivinhacao

def escolhe_jogo():

    print("********************************")
    print("*******Escolha o seu jogo*******")
    print("********************************")

    print("(1) forca (2) Advinhacao")

    jogo = int(input("Qual jogo?"))
    if(jogo == 1):
        print("jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando advinhacao")
        adivinhacao.jogar()

if(__nome__ == "__main__")
    escolhe_jogo()