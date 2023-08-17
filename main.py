from PySide2 import QtWidgets, QtCore, QtGui
import maya.cmds as cmds
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
import os
import json

from window_option import MyDialog


ROOT = str(os.path.dirname(__file__))


class My_Tab(MayaQWidgetDockableMixin, QtWidgets.QDockWidget):

    def __init__(self):

        super(My_Tab, self).__init__()

        self.setObjectName("My_Tab")

        self.setupUI()
        self.read_json()

    def setupUI(self):

        # window
        self.setMinimumWidth(200)
        self.setMaximumWidth(200)
        self.setMinimumHeight(500)
        self.setWindowTitle("Tool")
        self.setDockableParameters(widht=200)

        self.mainWidget = QtWidgets.QWidget()
        self.setWidget(self.mainWidget)

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        self.mainWidget.setLayout(self.mainLayout)
        # self.setLayout( self.mainLayout)

        # * scroll area
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setMinimumHeight(200)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_area_widget = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scroll_area_widget)
        self.scroll_layout = QtWidgets.QGridLayout()
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_layout.setContentsMargins(0, 0, 2, 0)
        self.scroll_layout.setSpacing(5)
        # * -> scroll_layout
        self.scroll_area_widget.setLayout(self.scroll_layout)
        self.mainLayout.addWidget(self.scrollArea)

        # button options

        self.option_btn = QtWidgets.QPushButton("Options")
        self.option_btn.clicked.connect(self.open_windowtool)
        self.mainLayout.addWidget(self.option_btn)

    def read_json(self):
        json_file_path = os.path.join(ROOT, "save.json")
        json_data = []
        if os.path.isfile(json_file_path):
            with open(json_file_path, 'r') as f:
                json_data = json.load(f)

        for entry in json_data:
            label = entry['label']
            button = QtWidgets.QPushButton(label)
            self.scroll_layout.addWidget(button)

    def open_windowtool(self):

        if cmds.window("MyDragDropWidgetID", exists=1):
            cmds.deleteUI("MyDragDropWidgetID")

        if cmds.windowPref("MyDragDropWidgetID", exists=1):
            cmds.windowPref("MyDragDropWidgetID", remove=1)

        # global myDragDialog
        self.myDragDialog = MyDialog()
        self.myDragDialog.show()


def main():

    if cmds.workspaceControl('My_TabWorkspaceControl', exists=True):
        cmds.deleteUI('My_TabWorkspaceControl', control=True)

    if cmds.workspaceControlState('My_TabWorkspaceControl', exists=True):
        cmds.workspaceControlState('My_TabWorkspaceControl', remove=1)

    myUI = My_Tab()
    myUI.show(dockable=True, area='right', allowedArea='right', floating=True)

    cmds.workspaceControl('My_TabWorkspaceControl',
                          label='My Tab',
                          edit=1,
                          tabToControl=['AttributeEditor', -1],
                          widthProperty='fixed',
                          initialWidth=250
                          )


main()
