#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set et sw=4 ts=4:

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from ddialog import DigitsDialog
from window import ReciterWindow
from digits import (num_names, num_digits, digits_length)

w = None
def showReciterWindow(number, end, offset, dark):
    global w
    # to compensate for the decimal point,
    # offset and need to be incremented unless they're 0
    if offset > 0: offset += 1
    if end < 2: end  = 1
    else      : end += 1
    txt = num_digits[number][offset:end]
    w = ReciterWindow(txt, dark)
    w.setWindowTitle("Reciting " + num_names[number])
    w.setWindowState(Qt.WindowMaximized)
    w.show()

def getArg(i):
    try: return sys.argv[i]
    except: return None

def getIntArg(i):
    try: return int(sys.argv[i])
    except: return None

def popArgValue(v):
    if v in sys.argv:
        sys.argv.remove(v)
        return True
    return False


app = QApplication(sys.argv)

dark = popArgValue('--dark') or popArgValue('-d')

number = getArg(1)
if number is not None:
    end = getIntArg(2)
    if end is None or end <= 0 or end > digits_length:
        end = digits_length
    offset = getIntArg(3)
    if offset is None or offset < 0 or offset >= digits_length:
        offset = 0
    showReciterWindow(number, end, offset, dark)
else:
    pass
    diag = DigitsDialog()
    diag.rejected.connect(sys.exit)
    diag.submit.connect(showReciterWindow)
    diag.open()

app.exit(app.exec_())
