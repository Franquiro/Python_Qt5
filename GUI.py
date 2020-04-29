from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import *

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('Cliqueaste el boton A')
    alert.exec_()

# Creo la aplicacion
app = QApplication([])
app.setStyle('Fusion')
app.setStyleSheet("QWidget{background-color:#333333; color:#FFFFFF;}")
# creo la ventana principal
window = QWidget()
# creo la etiqueta superior
label = QLabel()
label.setText('Hola')
# Creo los botones
btn_A = QPushButton('Boton A')
btn_B = QPushButton('Boton B')
# Creo un Layout
layout = QVBoxLayout()
# agrego los elementos al layout
layout.addWidget(label)
layout.addWidget(btn_A)
layout.addWidget(btn_B)
# conecto el boton A con el evento definido al principio
btn_A.clicked.connect(on_button_clicked)
# agrego el layout a la ventana
window.setLayout(layout)
#ejecuto la app
window.show()
app.exec_()

