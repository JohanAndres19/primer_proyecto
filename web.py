from flask  import Flask, render_template
from proyecto1 import Serenata

app = Flask(__name__)
@app.route('/')
def Index():
    return render_template('index.html')
    

if __name__ == "__main__":
    cancion = Serenata()
    app.run(port=8000, debug=True )
    

