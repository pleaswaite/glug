#!/bin/env python

import sys
import sqlite3
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = 'ui.ui'
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

def createDB():

    create_table_qsos = """CREATE TABLE IF NOT EXISTS qsos (
        id TEXT PRIMARY KEY,
        band TEXT NOT NULL,
        mode TEXT NOT NULL,
        time TEXT NOT NULL,
        mycall TEXT NOT NULL,
        myexchange TEXT NOT NULL,
        theircall TEXT NOT NULL,
        theirexchange TEXT NOT NULL,
        opcall TEXT NOT NULL
        );"""

    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute(create_table_qsos)

:class piloggergui(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.showMaximized()
        #read anything in LEs and look for dupes/other bands
        #while we're at it, check for unsent Qs and send to peers
#        self.log_button.clicked.connect(lambda: self.LogContact())
        #self.call_le.textChanged.connect(updateCallBox())

if __name__ == "__main__":



    app = QtGui.QApplication(sys.argv)
    window = piloggergui()
    window.show()
    sys.exit(app.exec_())
