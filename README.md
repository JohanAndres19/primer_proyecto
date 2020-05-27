# PRIMER PROYECTO: SERENATA
## Autores: Luis Guillermo Velez - Johan Aguirre Diaz

### Requerimientos
* **Tener instalado python 3.**
* **Tener instalado  flask.**

_Nota: si no se tiene instalado puede seguir el siguiente intructivo._ 


**Instalar python:**
1. Descargamos el instalador de python en [https://www.python.org/downloads/](https://www.python.org/downloads/).

![image012](imagenes/image012.gif)

2. Ejecutar el instalador e instalar python:

![image014](imagenes/image014.gif)


_Nota: Al instalar algunas versiones de python pueda que no venga con pip (paquete de instalacion para Python) asi la puede instalar._

**Instalar pip:**

1. Descargamos el archivo “get-pip.py”en: [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

![image016](imagenes/image016.gif)
2. En la terminal de windows y en la ruta donde tengamos el archivo anteriormente descargado ejecutamos el siguiente comando

       python get-pip.py
     
![image020](imagenes/image020.gif)

_Nota: Necesitaremos instalar Flask para conectar el frontend con el backend y  descargar la libreria numpy para poder generar numeros aleatorios ._

**Instalar Flask:**
En la terminal de windows ejecutamos el siguiente comando:

            pip install Flask
            
  ![image022](imagenes/image022.gif)
            
**Instalar numpy:**
Para instalar la libreria numpy,en la terminal de windows ejecutamos el siguiente comando:

            pip install numpy
            
   ![image024](imagenes/image024.gif)
   
### Situación problema:
Se quiere dar una serenata con un grupo integrado  con una cantidad de  músicos que varía entre los 5 a 10 integrantes y cada uno de ellos se le debe asignar un instrumento  de manera aleatoria.

### Analisis del problema:

![image002](imagenes/image002.gif)

Para esta situación los instrumentos que hemos escogido son los que ven en la imagen estos implementan  la interface la cual tiene los métodos Dibujar instru, tocar y Preparar Instrumento esto se sobre escriben en cada una de las clases de los instrumentos. 

### Principios utilizados:
##### Principio abierto/cerrado:
Este principio lo podemos ver ya que por el uso de interfaz para poder heredar los métodos  y poder sobre escribirlo en la clase del instrumento que se ponga. De esta forma podemos ver que se puede extender la cantidad de instrumentos sin tener que modificar el resto del código.

![image003](imagenes/image003.png)

#### Principio de responsabilidad única:
Este principio lo podemos evidenciar en la clase Serenata, que se encarga unicmante de iniciar la serenata con la lista ya retornada de las otras clases con los musicos y los instrumentos asignados.

![image004](imagenes/image005.png)

#### Principio de sustitución de liskov:
En este principio podemos evidenciar que las clases bateria,piano,saxofon,guitarra y violin heredan y utilizan todos los métodos de la clase instrumento, y no sobra ningún método.

![image008](imagenes/image008.gif)

![image010](imagenes/image010.gif)

### Manual de usuario:
La página tiene 3 botones:
* **Generar grupo.**
* **Preparar.**
* **Tocar.**

![image026](imagenes/image026.jpg)

1. El boton Generar grupo, Me generea aleatoriamente de 5 a 10 musicos y les asgina aleatoriamente uno de los 5 instrumentos posibles (bateria, piano, saxofon, guitarra, violin) y me los muestra en pantalla.

![image028](imagenes/image028.jpg)

2. El boton Preparar, Me genera un texto en pantalla que indica que los instrumentos generados con la instruccion "Generar grupo" ya han sido preparados.

![image030](imagenes/image030.jpg)

3. El boton tocar, Me genera un texto en pantalla que indica que los instrumentos preparados con la instruccion "Preparar" están siendo tocados.

![image032](imagenes/image032.jpg)

_Nota: Si la instruccion "Generar grupo" no se ha realizado, el boton "preparar" no hara nada, y a su vez si la instruccion "preparar" no se ha realizado el botón "tocar" no hara nada._
