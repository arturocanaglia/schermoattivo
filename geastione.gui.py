# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rosa/bin/Py/schermoAttivo/geastione.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(657, 390)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setSizeGripEnabled(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(180, 300, 261, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(140, 70, 381, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lblApp_2 = QtWidgets.QLabel(self.frame)
        self.lblApp_2.setGeometry(QtCore.QRect(20, 20, 91, 18))
        self.lblApp_2.setObjectName("lblApp_2")
        self.lblApp = QtWidgets.QLabel(self.frame)
        self.lblApp.setGeometry(QtCore.QRect(120, 90, 91, 18))
        self.lblApp.setObjectName("lblApp")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(120, 110, 113, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.singolo = QtWidgets.QCheckBox(self.frame)
        self.singolo.setGeometry(QtCore.QRect(120, 140, 121, 24))
        self.singolo.setChecked(True)
        self.singolo.setObjectName("singolo")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(240, 110, 41, 26))
        self.pushButton.setObjectName("pushButton")
        self.checkBoxAbilita = QtWidgets.QCheckBox(self.frame)
        self.checkBoxAbilita.setGeometry(QtCore.QRect(120, 180, 85, 24))
        self.checkBoxAbilita.setObjectName("checkBoxAbilita")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(10, 0, 102, 24))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(0, 180, 102, 24))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(0, 360, 102, 24))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_7 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_7.setGeometry(QtCore.QRect(550, 360, 102, 24))
        self.radioButton_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_8.setGeometry(QtCore.QRect(550, 0, 102, 24))
        self.radioButton_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_9 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_9.setGeometry(QtCore.QRect(550, 190, 102, 24))
        self.radioButton_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(280, 360, 102, 24))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_5.setGeometry(QtCore.QRect(280, 0, 102, 24))
        self.radioButton_5.setObjectName("radioButton_5")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblApp_2.setText(_translate("Dialog", "Area"))
        self.lblApp.setText(_translate("Dialog", "Applicazione"))
        self.singolo.setText(_translate("Dialog", "Singola istanza"))
        self.pushButton.setToolTip(_translate("Dialog", "cerca app file dialogo..."))
        self.pushButton.setText(_translate("Dialog", "..."))
        self.checkBoxAbilita.setText(_translate("Dialog", "Abilitata"))
        self.radioButton.setText(_translate("Dialog", "RadioButton"))
        self.radioButton_2.setText(_translate("Dialog", "RadioButton"))
        self.radioButton_3.setText(_translate("Dialog", "RadioButton"))
        self.radioButton_7.setText(_translate("Dialog", "RadioButton"))
        self.radioButton_8.setText(_translate("Dialog", "RadioButton"))
        self.radioButton_9.setText(_translate("Dialog", "RadioButton"))
        self.radioButton_4.setText(_translate("Dialog", "RadioButton"))
        self.radioButton_5.setText(_translate("Dialog", "RadioButton"))
