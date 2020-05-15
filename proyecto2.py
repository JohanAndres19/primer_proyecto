import numpy as np
import random

class Grupo_musical():
     def __init__(self):
         self.Orgarnizar_Grupo()

     def Orgarnizar_Grupo(self):
        num_musicos = random.randint(5,10)
        musicos_ins = []
        Instrumentos= np.array(["bateria","guitarra","piano","saxofon","violin"])
        for i in range (1,num_musicos):
            tipo_instru = random.randint(0,4)
            instru = Instrumentos[tipo_instru]  
            musicos_ins.append(instru)  
         
            
class Instrumento():
    def tocar(self):
        pass
    def PrepararInstrumento(self):
        pass
    
class bateria(Instrumento):
    def tocar(self):
        print(" preparando bateria ")

    def PrepararInstrumento(self):
        print(" preparando bateria ")

class piano(Instrumento):
    
    def PrepararInstrumento(self):
        print(" preparando piano ")

class saxofon(Instrumento):
     def PrepararInstrumento(self):
        print("preparando saxofon")

class guitarra(Instrumento):
    def PrepararInstrumento(self):
        print("preparando guitarra")

class violin(Instrumento):
    def PrepararInstrumento(self):
         print("preparando violin ")