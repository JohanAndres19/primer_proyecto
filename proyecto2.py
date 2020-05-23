import random
class Grupo_musical():
    def __init__(self):
         self.musicos_ins = []

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
    def Dibujar_indtru(self):
        pass
    def tocar(self):
        pass
    def PrepararInstrumento(self):
        pass
    
class bateria(Instrumento):
    def Dibujar_indtru(self):
        return"static/img/bateria.png"

    def tocar(self):
        return"tocando bateria"

    def PrepararInstrumento(self):
        return"preparando bateria "

class piano(Instrumento):
    def Dibujar_indtru(self):
        return"static/img/piano.jpg"

    def tocar(self):
        return"tocando piano"
    
    def PrepararInstrumento(self):
        return"preparando piano"

class saxofon(Instrumento):
    def Dibujar_indtru(self):
        return"static/img/saxofon.jpg"

    def tocar(self):
        return"tocando saxofon"

    def PrepararInstrumento(self):
        return"preparando saxofon"

class guitarra(Instrumento):
    def Dibujar_indtru(self):
        return"static/img/guitarra.jpg"

    def tocar(self):
        return"tocando guitarra"

    def PrepararInstrumento(self):
        return"preparando guitarra"

class violin(Instrumento):
    def Dibujar_indtru(self):
        return"static/img/Violin.jpg"
    def tocar(self):
        return"tocando violin"

    def PrepararInstrumento(self):
        return"preparando violin"