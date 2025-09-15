# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spectro.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

FUNCTIONAL_GROUPS = ["aromatics",
                    "alcohols",
                    "amines",
                    "esters",
                    "alkene",
                    "carb",
                    "ketones",
                    "phenol",
                    "nitriles",
                    "amides",
                    "aldehydes",
                    "alkyne"]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1913, 1142)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 50, 1381, 811))
        self.label.setMinimumSize(QtCore.QSize(1280, 720))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setStyleSheet("background: rgb(100,100,100);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 10, 221, 1021))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout.addWidget(self.pushButton_10)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout.addWidget(self.pushButton_12)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout.addWidget(self.pushButton_11)
        self.pushButton_14 = QtWidgets.QPushButton(self.widget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout.addWidget(self.pushButton_14)
        self.pushButton_13 = QtWidgets.QPushButton(self.widget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout.addWidget(self.pushButton_13)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1260, 960, 187, 57))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(990, 950, 211, 91))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(750, 960, 187, 57))
        self.pushButton_15.setObjectName("pushButton_15")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(1500, 900, 231, 141))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget_2)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(300, 40, 154, 631))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_28 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_28.setMinimumSize(QtCore.QSize(110, 110))
        self.pushButton_28.setMaximumSize(QtCore.QSize(180, 180))
        self.pushButton_28.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./pyQt5_metadata/icons/edit_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_28.setIcon(icon)
        self.pushButton_28.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_28.setObjectName("pushButton_28")
        self.verticalLayout_3.addWidget(self.pushButton_28, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_27 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_27.setMinimumSize(QtCore.QSize(110, 110))
        self.pushButton_27.setMaximumSize(QtCore.QSize(180, 180))
        self.pushButton_27.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./pyQt5_metadata/icons/trash_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_27.setIcon(icon1)
        self.pushButton_27.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_27.setObjectName("pushButton_27")
        self.verticalLayout_3.addWidget(self.pushButton_27, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1750, 970, 71, 57))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1913, 47))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "aromatics"))
        self.pushButton_6.setText(_translate("MainWindow", "alcohols"))
        self.pushButton_7.setText(_translate("MainWindow", "amines"))
        self.pushButton_8.setText(_translate("MainWindow", "esters"))
        self.pushButton_4.setText(_translate("MainWindow", "alkene"))
        self.pushButton_9.setText(_translate("MainWindow", "carb. acids"))
        self.pushButton_10.setText(_translate("MainWindow", "ketones"))
        self.pushButton_12.setText(_translate("MainWindow", "phenol"))
        self.pushButton_11.setText(_translate("MainWindow", "nitriles"))
        self.pushButton_14.setText(_translate("MainWindow", "amides"))
        self.pushButton_13.setText(_translate("MainWindow", "aldehydes"))
        self.pushButton_5.setText(_translate("MainWindow", "alkyne"))
        self.pushButton_3.setText(_translate("MainWindow", ">"))
        self.label_3.setText(_translate("MainWindow", "image file name"))
        self.pushButton_15.setText(_translate("MainWindow", "<"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "Go"))

    


# --- Add MainWindow subclass for scaling ---
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Store initial widget geometries for scaling
        self._base_geometries = {
            'label': QtCore.QRect(480, 50, 1381, 811),
            'widget': QtCore.QRect(70, 10, 221, 1021),
            'pushButton_3': QtCore.QRect(1260, 960, 187, 57),
            'label_3': QtCore.QRect(990, 950, 211, 91),
            'pushButton_15': QtCore.QRect(750, 960, 187, 57),
            'widget_2': QtCore.QRect(1500, 900, 231, 141),
            'widget_3': QtCore.QRect(300, 40, 154, 631),
            'pushButton_2': QtCore.QRect(1750, 970, 71, 57),
        }
        self._base_size = QtCore.QSize(1913, 1142)
        self.button_names = [
            'pushButton',      # aromatics
            'pushButton_6',    # alcohols
            'pushButton_7',    # amines
            'pushButton_8',    # esters
            'pushButton_4',    # alkene
            'pushButton_9',    # carb. acids
            'pushButton_10',   # ketones
            'pushButton_12',   # phenol
            'pushButton_11',   # nitriles
            'pushButton_14',   # amides
            'pushButton_13',   # aldehydes
            'pushButton_5',    # alkyne
        ]

    def resizeEvent(self, event):
        # Get new window size
        w = self.width()
        h = self.height()
        base_w = self._base_size.width()
        base_h = self._base_size.height()
        scale_w = w / base_w
        scale_h = h / base_h

        # Scale and set geometry for each widget
        for name, base_rect in self._base_geometries.items():
            widget = getattr(self.ui, name)
            new_rect = QtCore.QRect(
                int(base_rect.x() * scale_w),
                int(base_rect.y() * scale_h),
                int(base_rect.width() * scale_w),
                int(base_rect.height() * scale_h)
            )
            widget.setGeometry(new_rect)

        # Optionally, scale font sizes (simple example)
        font = self.font()
        font.setPointSize(int(10 * min(scale_w, scale_h)))
        self.setFont(font)

        super().resizeEvent(event)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

