class Pessoa():

    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

        self.dormindo = False
        self.falando = False
        self.comendo = False

    def comer(self,comida):
        if(self.dormindo == True):
            print(f"{self.nome}Não pode comer porque está dormindo")
        elif(self.falando == True):
            print(f"{self.nome}'Não pode comer porque está falando")
        else:
           self.comendo = True
        print(f'{self.nome} está comendo {comida}.')

    def falar(self,fala):
        if(self.dormindo == True):
            print(f"{self.nome}Não pode falar porque está dormindo")
        elif(self.comendo == True):
            print(f"{self.nome} Não pode falar porque está comendo")
        else:
            self.falando = True
            print(f"{self.nome} está falando {fala}.")


    def dormir(self):
         if (self.falando == True):
            print(f"{self.nome}Não pode dormir porque está falando")
         elif (self.comendo == True):
            print(f"{self.nome} Não pode dormir porque está comendo")
         else:
             self.dormindo = True
             print(f"{self.nome} foi dormir")

    def pararComer(self):
        self.comendo = False
        print(f"{self.nome} parou de comer")

    def pararFalar(self):
        self.falando = False
        print(f"{self.nome} parou de falar")

    def pararDormir(self):
        self.dormindo = False
        print(f"{self.nome} acordou")




