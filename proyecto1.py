from proyecto2 import * 

class Serenata ():   
   def __init__(self):
      self.grupo = Grupo_musical()
      self.lista=[]
 
   def Armar_Grupo(self):
      if len(self.lista)== 0:      
        self.grupo.Orgarnizar_Grupo()
        self.lista = self.grupo.Get_musicos()
        print("esta entrado porque no hay nada ")         
      return self.lista

   def Dar_serenata(self,opcion,lista1):
     musicos =[]  
     if opcion is 0:
            for i in lista1:
              musicos.append(i.Dibujar_indtru())
     elif opcion is 1: 
            for i in lista1:
              musicos.append(i.Dibujar_indtru())
            for i in lista1:
              musicos.append(i.PrepararInstrumento())  
     elif opcion is 2:   
            for i in lista1:
              musicos.append(i.Dibujar_indtru())
            for i in lista1:
               musicos.append(i.tocar())            
     return musicos


     