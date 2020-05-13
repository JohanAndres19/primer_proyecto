import numpy as np
import random

class Grupo_musical():
     
     def Armar_Grupo(self):
        num_musicos = random.randint(5,10)
        tipo_instru = random.randint(0,4)
        #ins = Instrumento()
        # Instrumentos= np.array(["bateria","guitarra","piano","saxofon","violin"])
        print(num_musicos,tipo_instru)

class Instrumento():
    def tocar(self):
        pass
    def PrepararInstrumento(self):
        pass
    def Obtener_instrumento(self):
        pass

class bateria(Instrumento):
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