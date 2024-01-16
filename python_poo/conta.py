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
    
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, saldo):
        self.__saldo = saldo
    
    def get_titular(self):
        return self.__titular
    
    def set_titular(self, titular):
        self.__titular = titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    @staticmethod
    def codigos_bancos():
        return {"BB" : '001', "Caixa":'104', "Bradesco":'237'}