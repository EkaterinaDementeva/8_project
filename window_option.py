from PySide2 import QtWidgets, QtCore
import maya.cmds as cmds
import os
import json


from WidgetField import WidgetField

ROOT = str(os.path.dirname(__file__))


class MyDialog(QtWidgets.QDialog):

    def __init__(self):
        super(MyDialog, self).__init__()

        self.setObjectName("MyDragDropWidgitID")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setMinimumSize(500, 500)
        self.setWindowTitle("Drag an d Drop")
        self.create_content()
        # self.read_json()
    

    def read_json(self):
        json_file_path = os.path.join(ROOT, "save.json")
        json_data = []
        if os.path.isfile(json_file_path):
            with open(json_file_path, 'r') as f:
                json_data = json.load(f)
        return json_data
    
    def create_content(self):
        # add layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.main_layout)
      
        self.field_layout = QtWidgets.QHBoxLayout()
                
        json_data = self.read_json()
        list_of_saved_buttons = []
        for a in json_data:
            list_of_saved_buttons.append(a['label'])

        self.w_1 = WidgetField()
        self.w_2 = WidgetField()

        for i in range(5):
            self.text_button = "Button {}".format(i)
            if self.text_button in list_of_saved_buttons:
                self.w_2.feedButtons(self.text_button)
                continue
            self.w_1.feedButtons(self.text_button)

        self.field_layout.addWidget(self.w_1)
        self.field_layout.addWidget(self.w_2)
        
        self.main_layout.addLayout(self.field_layout)

        # save button
        self.btn_save = QtWidgets.QPushButton("Save")
        self.btn_save.clicked.connect(self.save_json)
        self.main_layout.addWidget(self.btn_save)

    
    def save_json(self):
        """ check items in right margin and save to file """
        output = []
        
        if self.w_2.scroll_layout.count():
            for i in range(self.w_2.scroll_layout.count()):
                item = self.w_2.scroll_layout.itemAt(i)
                widget = item.widget()
                label = widget.label.text()
                output.append({"label": label})

        json_file_path = os.path.join(ROOT, "save.json")
        with open(json_file_path, 'w') as outfile:
            json.dump(output, outfile, indent=4)
        self.close()
