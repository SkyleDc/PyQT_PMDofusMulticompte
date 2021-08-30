import sys
from collections import namedtuple

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import win32gui
from pynput.keyboard import Listener
import icon


def isrunning():
    tasklist = QProcess()
    tasklist.start('tasklist /v /fo list /fi \"imagename eq dofus.exe\"')
    tasklist.waitForStarted()
    tasklist.waitForFinished()
    tasklist.waitForReadyRead()
    output = tasklist.readAllStandardOutput()
    tasklist.close()

    return str(output)


def on_press(key):
    print("PRESSED", key)


with Listener(on_press=on_press) as listener:
    class Ui(QMainWindow):
        def __init__(self):
            super(Ui, self).__init__()  # Call the inherited classes __init__ method
            uic.loadUi('mainwindow.ui', self)  # Load the .ui file
            self.show()  # Show the GUI
            self.setWindowIcon(QIcon(":PMMultiCompteDofus.ico"))

            MyStruct = namedtuple('DataDofus', ['PID', 'Window_Name'])

            outputdofus = isrunning().split("\\r\\n")

            while '' in outputdofus:
                outputdofus.remove('')
            while '"' in outputdofus:
                outputdofus.remove('"')
            while 'b"' in outputdofus:
                outputdofus.remove('b"')

            nbdofus = int(len(outputdofus) / 9)

            tableaudofus = []

            if nbdofus != 0:
                for x in range(nbdofus - 1, -1, -1):
                    for y in range(0, 6):
                        test = int((x * 8) + 2 + x)
                        outputdofus.pop(test)

                for x in range(0, nbdofus):
                    a = outputdofus[1].split(":")
                    a = a[1].split(" ")
                    while '' in a:
                        a.remove('')
                    a = int(a[0])

                    b = outputdofus[2].split(":")
                    b = b[1]
                    b = str(b[1:])

                    structsingledofus = MyStruct(a, b)
                    tableaudofus.append(structsingledofus)

                    del outputdofus[0:3]

            print(tableaudofus)

            if nbdofus == 0:
                self.TabDofus.addTab(QWidget(), "Aucun Dofus.exe lancé")
            else:
                for x in range(0, nbdofus):
                    hwnd = win32gui.FindWindow(None, str(tableaudofus[x].Window_Name))
                    m_window = QWindow.fromWinId(hwnd)

                    m_widget = QWidget.createWindowContainer(m_window, self)
                    self.TabDofus.addTab(m_widget, tableaudofus[x].Window_Name)


    app = QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())

    listener.join()
