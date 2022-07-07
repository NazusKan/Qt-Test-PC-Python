from PyQt5 import QtWidgets, uic
import psutil

battery = psutil.sensors_battery()
app = QtWidgets.QApplication([])

ui = uic.loadUi("main.ui")
net = 100
com = 50

def ButtonStart():
	ui.progressBar.setValue(net)

def ButtonStop():
	ui.progressBar.setValue(com)

def horizontalSlider(horizontalSlider):
	ui.progressBar.setValue(horizontalSlider)

def label():
	ui.label.setText(battery.percent)

def convertTime(seconds):
  minutes, seconds = divmod(seconds, 60)
  hours, minutes = divmod(minutes, 60)
  return "%d:%02d:%02d" % (hours, minutes, seconds)

ui.ButtonStart.clicked.connect(ButtonStart)
ui.ButtonStop.clicked.connect(ButtonStop)
ui.horizontalSlider.valueChanged.connect(horizontalSlider)
ui.labelPercentage.setText(str(battery.percent))
ui.labelPlugged.setText(str(battery.power_plugged))
ui.labelLeft.setText(convertTime(battery.secsleft))

ui.show()
app.exec()
