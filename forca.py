def jogar():

    print("********************************")
    print("bem vindo ao jogo de forca")
    print("********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    while(not acertou and not enforcou):
        chute = input("Qual letra?")
        chute = chute.strip().upper()
        index = 0

        if(chute in palavra_secreta):

            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index = index +1
            else:
                erros += 1

            enforcou = erros == 6
            acertou = "_" not in letras_acertadas
            print(letras_acertadas)

            if(acertou):
                print("voce ganhou")
            else:
                print("voce perdeu")
            


      

        print(letras_acertadas) 

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()