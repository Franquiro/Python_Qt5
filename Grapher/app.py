from PyQt5 import QtWidgets, uic, QtCore
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import sys
import serial

ser = serial.Serial(port = '/dev/rfcomm0', baudrate = 9600 , bytesize = 8, timeout = 2 , stopbits = serial.STOPBITS_ONE)
pg.setConfigOptions(antialias=True)
class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow,self).__init__(*args,**kwargs)
		
		uic.loadUi("grapher.ui",self)
		self.x = []
		self.y = []
		self.pen1 = pg.mkPen(width=1.738,color=(80, 255, 255))
		self.pen2 = pg.mkPen(width=1.738,color="#6FEB09")
		self.pen3 = pg.mkPen(width=1.738,color="#FF002F")#E8002B")#C20022")
		self.pen4 = pg.mkPen(width=1.738,color="#FFCC00")
		self.plot(self.x,self.y)
		

		self.timer = QtCore.QTimer()
		self.timer.setInterval(1)
		self.timer.timeout.connect(self.update_plot)
		self.timer.start()

		self.start_btn.clicked.connect(self.start_plot)
		self.stop_btn.clicked.connect(self.stop_plot)
		self.rX_btn.clicked.connect(self.reset_x)
		


	def plot(self,x,y):
		self.curve = self.graphWidget.plot(self.x,self.y,pen=self.pen4)
		self.graphWidget.setBackground('#232323')
		self.graphWidget.showGrid(x = True, y = True, alpha = 0.5)
	def reset_x(self):
		self.X_dial.setValue(0)
		
	def update_plot(self):
		if(ser.in_waiting > 0):
			
			self.puntos = 100 + self.X_dial.value()
			self.X_label.setText(str(self.puntos)+" dots")
			if(len(self.x) > self.puntos):
				self.x = self.x[len(self.x)-self.puntos:]
				self.y = self.y[len(self.y)-self.puntos:]

			serialString = ser.readline()
			try:
				serialNum = float(serialString.decode("Ascii"))
				self.y.append(serialNum)
				if len(self.x) == 0:
					self.x.append(0)
				else:
					self.x.append(self.x[-1]+1)
				print(serialNum)
				self.curve.setData(self.x,self.y)
			except ValueError:
				print("Value Unparseable")
			
	def stop_plot(self):
		self.timer.stop()
		
	def start_plot(self):
		self.timer.start()
	

	
def main():
	app = QtWidgets.QApplication(sys.argv)
	main = MainWindow()
	main.show()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
