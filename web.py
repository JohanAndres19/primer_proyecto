from flask  import Flask, render_template,request
from proyecto1 import Serenata

app = Flask(__name__)
sere= Serenata()
@app.route('/',methods=['GET','POST'])
def Index():
   if request.method == 'POST':
       listai=[]
       image=[]
       accion=[]
       if request.form.get('Generar grupo')=='Generar grupo':
            sere.Set_lista(listai)
            listai= Serenata().Dar_serenata(0,sere.Armar_Grupo())
       elif request.form.get('Preparar')=='Preparar':
            listai=Serenata().Dar_serenata(1,sere.Armar_Grupo())
       elif request.form.get('tocar')=='tocar':
            listai= Serenata().Dar_serenata(2,sere.Armar_Grupo()) 
       for i in listai:
               if i.find("static")==0:
                    image.append(i)
               else:
                    accion.append(i)     
       largoi=len(image) 
       largoa=len(accion)         
       data=zip(image,accion) 
       return render_template('index.html',image=image,accion=accion,largoa=largoa,largoi=largoi, data=data)     
   else:    
       return render_template('index.html',image=[],accion=[],largoa=0,largoi=0)
       
if __name__ == "__main__":
    app.run(port=8000, debug=True )
    
    
