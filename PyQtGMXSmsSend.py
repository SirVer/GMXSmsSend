#!/usr/bin/env python
# encoding: utf-8

import sys
import time

from PyQt4.QtCore import *
from PyQt4.QtGui import *
# from PyQt4.QEvent import *


from GMXSSMSSendDialog import Ui_GMXSMSSendDialog

from Sms import GMXSmsSender

class LoginThread(QThread):
    def __init__(self, sms, parent = None):
        QThread.__init__(self, parent)

        self._s = sms

    def run(self):
        try:
            for i in self._s.next_login_step():
                self.emit(SIGNAL("statusUpdate"), i)
        except Exception, e:
            self.emit(SIGNAL("statusError"), e)
            return

        self.emit(SIGNAL("statusDone"), i)

class GMXSmsWindow(QMainWindow, Ui_GMXSMSSendDialog):
    def __init__(self, parent, size, number = ""):
        super(GMXSmsWindow, self).__init__(parent)

        self.setupUi(self)

        self.setWindowTitle("Send GMX SMS")

        if number != "":
            self.textEdit.setFocus()
            self.numberEdit.setText(number)
        else:
            self.numberEdit.setFocus()

        self._s = GMXSmsSender()

        # Install eventfilter for our textedit
        self.textEdit.installEventFilter(self)

        self._ready_to_send = False

        self._worker = LoginThread(self._s)
        self.connect(self._worker, SIGNAL("statusUpdate"), self.statusUpdate)
        self.connect(self._worker, SIGNAL("statusError"), self.statusError)
        self.connect(self._worker, SIGNAL("statusDone"), self.statusDone)
        self._worker.start()

        # self.statusTimer = QTimer()
        # self.connect(self.statusTimer, SIGNAL("timeout()"), self.statusTimeout)
        # self.statusTimer.start(200)


    def updateUi(self):
        num = unicode(self.numberEdit.text())
        text = unicode(self.textEdit.toPlainText())

        enable_but =  True if len(num) and len(text) and self._ready_to_send \
            else False
        self.sendButton.setEnabled(enable_but)

    def eventFilter(self, obj, ev):
        if ev.type() == QEvent.KeyPress:
            if ev.key() == Qt.Key_Return:
                self.on_sendButton_pressed()
                return True
            return False
        return QMainWindow.eventFilter(self, obj, ev)

    def statusUpdate(self, st):
        lookup = {
            "started": "1/4 Logging in to GMX",
            "logged in": "2/4 Going to SMS Page",
            "on sms page": "3/4 Going to SMS Manager",
            "on sms manager page": "4/4 Following last redirect"
        }

        self.statusLabel.setText(lookup.get(st,""))

    def statusError(self, e):
        QMessageBox.critical( self, "Error:", "Error:\n" + str(e))
        self.close()

    def statusDone(self):
        self.statusLabel.setText(u"Verbleibende SMS diesen Monat:")
        self.remainingSmsLabel.setText("%i / %i" % self._s.freesms)

        self._ready_to_send = True

        self.updateUi()

    def on_sendButton_pressed(self):
        mynr = unicode(self.numberEdit.text())
        mytext = unicode(self.textEdit.toPlainText())

        if not self.sendButton.isEnabled():
            return

        self.sendButton.setEnabled(False)

        try:
            self._s.send_sms(  mynr, mytext )
            self.close()
        except Exception, e:
            QMessageBox.critical( self, "Es traten Fehler beim Senden auf:",
                str(e))
            self.close()
            try:
                self._s.logout()
            except:
                pass

            return

    def on_menuClose_triggered(self):
        self.close()

    def on_numberEdit_textEdited(self):
        self.updateUi()
    def on_textEdit_textChanged(self):
        self.updateUi()

        zeichen = len(unicode(self.textEdit.toPlainText()))

        sms = 1
        if zeichen > 160:
            sms = 2
        if zeichen > 160+145:
            sms = 3
        if zeichen > 160+145+152:
            sms = "4 or more"

        self.nSmsLabel.setText( str(sms) )
        self.nCharsLabel.setText( "%i" % zeichen )




def main( argv ):
    "Show the window"

    number = ""
    if os.path.exists("/tmp/phone_data"):
        f = open("/tmp/phone_data")
        number = f.readline()
        f.close()
        os.remove("/tmp/phone_data")

    app = QApplication(sys.argv)
    win = GMXSmsWindow(None,
        size = (420,600),  # Good for my 1280x800 resolution
        number = number,
        )

    win.show()
    win.raise_()

    sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    import os

    main( sys.argv )


