from PyQt6.QtWidgets import QApplication, QMainWindow

from Ex124.Ex124.MainWindowEx import MainWindowEx

app=QApplication([])
myWindow=MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()