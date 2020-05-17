from flask  import Flask, render_template, request
from proyecto1 import Serenata

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def Index():
  image=[]
  accion=[]
  if request.method == 'POST':
       if request.form.get('Generar grupo')=='Generar grupo':
            image= Serenata().Armar_Grupo()
       elif request.form.get('Preparar')=='Preparar':
            accion=Serenata().Dar_serenata(0)
       elif request.form.get('tocar')=='tocar':
            accion= Serenata().Dar_serenata(1)    
  a=len(image)
  b=len(accion)      
  return render_template('index.html', accion=accion ,image= image,a=a,b=b)
    

if __name__ == "__main__":
    app.run(port=8000, debug=True )
    
