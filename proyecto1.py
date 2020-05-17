from proyecto2 import * 

class Serenata ():   
   def __init__(self):
      self.grupo = Grupo_musical()

   def Armar_Grupo (self):
      self.grupo.Orgarnizar_Grupo()
      lista= []
      for i in self.grupo.Get_musicos():
        lista.append(i.Dibujar_indtru())
      print(len(lista))  
      return lista  
      
   def Dar_serenata(self,opcion):
     lista =[]
     musicos =self.grupo.Get_musicos()
     if opcion is 1:
            for i in musicos:
              lista.append(i.tocar())
     elif opcion is 0: 
            for i in musicos:
             lista.append(i.PrepararInstrumento())  
     elif opcion is 2:   
            for i in musicos:
               lista.append(i.Dibujar_indtru())    
     return lista


     