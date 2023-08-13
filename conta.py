class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
       print("construindo objeto...")
       self.__numero = numero
       self.__titular = titular
       self.__saldo = saldo
       self.__limite = limite

    def estrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo,self.__titular))
    
    def deposita(self,valor):
        self.__saldo += valor
    
    def saca(self, valor):
        self.__saldo -= valor
    
    