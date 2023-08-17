from PySide2 import QtWidgets, QtCore, QtGui
import maya.cmds as cmds

from WidgetButton import WidgetButton
# from WidgetButton import MyMIME

class WidgetField(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WidgetField, self).__init__()

        self.buttonsList = []

        # Some settings
        self.setFixedSize(240, 490)
        # this is important - we can now drop widgets here
        self.setAcceptDrops(True)

        # Add background color
        self.setAutoFillBackground(True)
        color = 40
        self.p = self.palette()
        self.p.setColor(
            self.backgroundRole(),
            QtGui.QColor(color, color, color)
            )
        self.setPalette(self.p)

        # Let's add main layout
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)

        # * scroll area
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setMinimumHeight(200)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_area_widget = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scroll_area_widget)
        self.scroll_layout = QtWidgets.QGridLayout()
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_layout.setContentsMargins(0, 0, 2, 0)
        self.scroll_layout.setSpacing(5)
        # * -> scroll_layout
        self.scroll_area_widget.setLayout(self.scroll_layout)
        self.mainLayout.addWidget(self.scrollArea)

              
    def feedButtons(self, text_button):
        # # We will create Drag&Drop buttons here

        self.button = WidgetButton()
        self.button.addLabel(t=text_button)
        self.scroll_layout.addWidget(self.button)


    '''DRAG & DROP'''

    def dragEnterEvent(self, e):
        # what happens when we start dragging our mouse
        # e - is QDragEnterEvent
        e.acceptProposedAction()  # accept dragEnter action

    def dropEvent(self, e):

        # pos = e.scenePos() # get position where we released mouse button
        mimeData = e.mimeData()  # get mime data from the cursor
        mimeText = mimeData.getText()
        # mimeFrom = mimeData.getFrom()
        # print (e.source, self)
        e.source().deleteLater()

        # recreate button with Mime text and other data
        button = WidgetButton()
        button.addLabel(t=mimeText)
        self.scroll_layout.addWidget(button)

    def dragMoveEvent(self, e):
        e.acceptProposedAction()
