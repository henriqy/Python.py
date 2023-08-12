class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
       print("construindo objeto...")
       self.numero = numero
       self.titular = titular
       self.saldo = saldo
       self.limite = limite

    def estrato(self):
        print("Saldo de {} do titular {}".format(self.saldo,self.titular))
    
    def deposita(self,valor):
        self.saldo += valor
    
    def saca(self, valor):
        self.saldo -= valor
    
    