from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import serial
from random import randint

ser = serial.Serial(port = '/dev/ttyUSB0', baudrate = 9600 , bytesize = 8, timeout = 2 , stopbits = serial.STOPBITS_ONE)


class MainWindow(QtWidgets.QMainWindow):

	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		
		self.graphWidget = pg.PlotWidget()
		self.setCentralWidget(self.graphWidget)
		self.x = [0]  # 100 time points
		self.y = [0]  # 100 data points
		self.graphWidget.setBackground('#333333')
		self.graphWidget.showGrid(x = True, y = True, alpha = 0.3)
		

		pen = pg.mkPen(color=(20, 255, 255))
		self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)
 # ... init continued ...
		self.timer = QtCore.QTimer()
		self.timer.setInterval(1)
		self.timer.timeout.connect(self.update_plot_data)
		self.timer.start()

		

			

	def update_plot_data(self):
		if(ser.in_waiting > 0):
			if(len(self.x) > 100):
				self.x = self.x[1:]
				self.y = self.y[1:]
			serialString = ser.readline()
			serialNum = float(serialString.decode("Ascii"))
			self.y.append(serialNum)
			self.x.append(self.x[-1]+1)
		

			self.data_line.setData(self.x, self.y)  # Update the data.

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
