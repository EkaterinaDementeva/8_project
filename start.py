from PySide2 import QtWidgets, QtCore, QtGui
import maya.cmds as cmds

import sys

sys.path.append('C:/Users/Admin/Documents/Maya/scripts/DragandDropSample')

import DragandDropSample.main

if 'DragandDropSample' in sys.modules:
    print("Reloading DragandDropSample")
    import importlib
    importlib.reload(DragandDropSample.main)
    