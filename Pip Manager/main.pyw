from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox
import os
from pyautogui import alert as a
Form, Window = uic.loadUiType("gui.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

InstallOperation = "Install"
UpdateOperation = "Update"
DeleteOperation = "Delete"

form.DeleteLine.setPlaceholderText("Your Module")
form.UpdateLine.setPlaceholderText("Your Module")
form.InstallLine.setPlaceholderText("Your Module")
form.Run.setToolTip("Starts Programm")
form.Info.setToolTip("Get Info")

def Install():
    InstallData = form.InstallLine.text()
    UpdateData = form.UpdateLine.text()
    DeleteData = form.DeleteLine.text()
    if InstallData == "":
        None
    else:
        a("Installing...", "Pip Manager")
        os.system("pip install " + InstallData)
        a(f"Operation For \"{InstallOperation}\" Has Been Completed", "Pip Manager")
    if UpdateData == "":
        None
    else:
        a("Updating...", "Pip Manager")
        os.system("pip install --upgrade " + UpdateData)
        a(f"Operation For \"{UpdateOperation}\" Has Been Completed", "Pip Manager")
    if DeleteData == "":
        None
    else:
        a("Deleting...", "Pip Manager")
        os.system("pip uninstall " + DeleteData)
        a(f"Operation For \"{DeleteOperation}\" Has Been Completed", "Pip Manager")

def GetInfo():
    a("Programm created for pip managment, and just for facilities. \n Language - Python \n Author: Ivan Perzinskiy", "Pip Manager")

form.Run.clicked.connect(Install)
form.Info.clicked.connect(GetInfo)

app.exec_()
