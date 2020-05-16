from proyecto2 import * 

class Serenata ():   
   def __init__(self):
      self.Armar_Grupo()

   def Armar_Grupo (self):
       self.grupo = Grupo_musical()
      
   def Dar_serenata(self,opcion):
     musicos =self.grupo.Get_musicos()
    
     if opcion is 1:
            for i in musicos:
              i.tocar()
     else : 
            for i in musicos:
              i.PrepararInstrumento()  
 

if __name__ == "__main__":
    sere = Serenata()
    print("ingrse 1 o 0")
    num =int( input())
    sere.Dar_serenata(num)
     