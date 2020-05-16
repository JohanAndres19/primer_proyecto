import random
class Grupo_musical():
    def __init__(self):
         self.musicos_ins = []
         self.Orgarnizar_Grupo()

    def Orgarnizar_Grupo(self):
        num_musicos = random.randint(5,10) 
        Instrumentos= [bateria(),guitarra(),piano(),saxofon(),violin()]
        for i in range (1,num_musicos):
            tipo_instru = random.randint(0,4)
            instru = Instrumentos[tipo_instru]  
            self.musicos_ins.append(instru) 

    def Get_musicos(self):
        return self.musicos_ins
            
class Instrumento():
    def tocar(self):
        pass
    def PrepararInstrumento(self):
        pass
    
class bateria(Instrumento):
    def tocar(self):
        print(" tocando bateria ")

    def PrepararInstrumento(self):
        print(" preparando bateria ")

class piano(Instrumento):
    def tocar(self):
        print(" tocando piano ")
    
    def PrepararInstrumento(self):
        print(" preparando piano ")

class saxofon(Instrumento):
    def tocar(self):
        print(" tocando saxofon ")

    def PrepararInstrumento(self):
        print("preparando saxofon")

class guitarra(Instrumento):
    def tocar(self):
        print(" tocando guitarra ")

    def PrepararInstrumento(self):
        print("preparando guitarra")

class violin(Instrumento):
    def tocar(self):
        print(" tocando violin ")

    def PrepararInstrumento(self):
         print("preparando violin ")