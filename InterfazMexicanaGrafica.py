#Implementamos una interfaz gráfica para festejar este 15 de septiembre. ¡Qué mejor forma de hacerlo (y obtener buena calificación en el curso...)! :)
import sys
import time
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from datetime import date

#Función que calcula cuántos días faltan para el siguiente 15 de septiembre.
def diasParaIndependencia():
	hoy= date.today() #Obtenemos la fecha de el día de hoy.
	dia_independencia= date(hoy.year, 9, 15) #La fecha en que es día de independencia este año.
	if dia_independencia < hoy: #Esta instrucción es la que lo hace dinámico, si ya pasó la fecha pues sumamos un año a la fecha del día festivo.
		dia_independencia= dia_independencia.replace(year= hoy.year + 1)
	dias_faltantes= abs(dia_independencia - hoy) #Obtenemos los días que nos faltan.
	boton.setText("Los días faltantes para el próximo 15 de septiembre son (¡sin contar el día de hoy!):   "+ str(dias_faltantes.days)+" día(s)")
	boton.resize(boton.sizeHint())
	boton.move(75, 250)
	
app= QApplication(sys.argv) #Creamos la App.
window= QWidget() 
window.resize(800, 500)
window.setWindowTitle("¡Viva México!")	#Ventana y propiedades de esta.

#Agregamos un Background.
fondo = QPalette()
fondo.setBrush(QPalette.Background, QBrush(QPixmap("Background.jpg")))
window.setPalette(fondo)

#Agregamos el ícono.
icono= QtGui.QIcon('IconoInterfaz.jpeg')
window.setWindowIcon(icono)

#Creamos una etiqueta, le ponemos texto, color, la alineamos y la añadimos a nuestra caja de Widgets.
colores = QtGui.QPalette()
colores.setColor(QtGui.QPalette.Foreground, QtCore.Qt.white)
pj_importantes= QLabel()
pj_importantes.setText("A continuación te mostramos 3 personajes importantes de la Independencia de México: \n\n1.- Miguel Hidalgo y Costilla (1753 – 1811) \n\n2.- Josefa Ortiz de Domínguez (1768 – 1829) \n\n3.- Vicente Guerrero (1782 – 1830)")
pj_importantes.setAlignment(Qt.AlignCenter)
pj_importantes.setPalette(colores)
caja = QVBoxLayout()
caja.addWidget(pj_importantes)
caja.addStretch()

#Creamos el botón, añadiéndole su escucha correspondiente, dimensión, etc.
boton= QPushButton('APRIÉTAME', window) #Tuve duda si era aprétame o apriétame... Yahoo me respaldó  ~o~
boton.resize(boton.sizeHint())
boton.move(350, 250)
boton.clicked.connect(diasParaIndependencia)

#Agregamos todos los widgets y mostramos la ventana.
window.setLayout(caja)
window.show()
sys.exit(app.exec_())