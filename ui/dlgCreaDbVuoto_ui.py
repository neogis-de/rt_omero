# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/dlgCreaDbVuoto.ui'
#
# Created: Tue May  6 13:20:53 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(589, 370)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.shape1Group = QtGui.QGroupBox(Dialog)
        self.shape1Group.setCheckable(True)
        self.shape1Group.setObjectName(_fromUtf8("shape1Group"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.shape1Group)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_1 = QtGui.QHBoxLayout()
        self.horizontalLayout_1.setObjectName(_fromUtf8("horizontalLayout_1"))
        self.label_9 = QtGui.QLabel(self.shape1Group)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_1.addWidget(self.label_9)
        self.filename1Edit = QtGui.QLineEdit(self.shape1Group)
        self.filename1Edit.setReadOnly(True)
        self.filename1Edit.setObjectName(_fromUtf8("filename1Edit"))
        self.horizontalLayout_1.addWidget(self.filename1Edit)
        self.browse1Btn = QtGui.QToolButton(self.shape1Group)
        self.browse1Btn.setObjectName(_fromUtf8("browse1Btn"))
        self.horizontalLayout_1.addWidget(self.browse1Btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.shape1Group)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.field1Combo = QtGui.QComboBox(self.shape1Group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.field1Combo.sizePolicy().hasHeightForWidth())
        self.field1Combo.setSizePolicy(sizePolicy)
        self.field1Combo.setObjectName(_fromUtf8("field1Combo"))
        self.horizontalLayout.addWidget(self.field1Combo)
        self.label = QtGui.QLabel(self.shape1Group)
        self.label.setIndent(20)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.prefix1Combo = QtGui.QComboBox(self.shape1Group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefix1Combo.sizePolicy().hasHeightForWidth())
        self.prefix1Combo.setSizePolicy(sizePolicy)
        self.prefix1Combo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.prefix1Combo.setObjectName(_fromUtf8("prefix1Combo"))
        self.prefix1Combo.addItem(_fromUtf8(""))
        self.prefix1Combo.addItem(_fromUtf8(""))
        self.prefix1Combo.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.prefix1Combo)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.shape1Group)
        self.shape2Group = QtGui.QGroupBox(Dialog)
        self.shape2Group.setCheckable(True)
        self.shape2Group.setChecked(False)
        self.shape2Group.setObjectName(_fromUtf8("shape2Group"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.shape2Group)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_7 = QtGui.QLabel(self.shape2Group)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.filename2Edit = QtGui.QLineEdit(self.shape2Group)
        self.filename2Edit.setReadOnly(False)
        self.filename2Edit.setObjectName(_fromUtf8("filename2Edit"))
        self.horizontalLayout_3.addWidget(self.filename2Edit)
        self.browse2Btn = QtGui.QToolButton(self.shape2Group)
        self.browse2Btn.setObjectName(_fromUtf8("browse2Btn"))
        self.horizontalLayout_3.addWidget(self.browse2Btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.shape2Group)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.field2Combo = QtGui.QComboBox(self.shape2Group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.field2Combo.sizePolicy().hasHeightForWidth())
        self.field2Combo.setSizePolicy(sizePolicy)
        self.field2Combo.setObjectName(_fromUtf8("field2Combo"))
        self.horizontalLayout_2.addWidget(self.field2Combo)
        self.label_4 = QtGui.QLabel(self.shape2Group)
        self.label_4.setIndent(20)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.prefix2Combo = QtGui.QComboBox(self.shape2Group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefix2Combo.sizePolicy().hasHeightForWidth())
        self.prefix2Combo.setSizePolicy(sizePolicy)
        self.prefix2Combo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.prefix2Combo.setObjectName(_fromUtf8("prefix2Combo"))
        self.prefix2Combo.addItem(_fromUtf8(""))
        self.prefix2Combo.addItem(_fromUtf8(""))
        self.prefix2Combo.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.prefix2Combo)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.shape2Group)
        self.shape3Group = QtGui.QGroupBox(Dialog)
        self.shape3Group.setCheckable(True)
        self.shape3Group.setChecked(False)
        self.shape3Group.setObjectName(_fromUtf8("shape3Group"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.shape3Group)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_8 = QtGui.QLabel(self.shape3Group)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_4.addWidget(self.label_8)
        self.filename3Edit = QtGui.QLineEdit(self.shape3Group)
        self.filename3Edit.setReadOnly(True)
        self.filename3Edit.setObjectName(_fromUtf8("filename3Edit"))
        self.horizontalLayout_4.addWidget(self.filename3Edit)
        self.browse3Btn = QtGui.QToolButton(self.shape3Group)
        self.browse3Btn.setObjectName(_fromUtf8("browse3Btn"))
        self.horizontalLayout_4.addWidget(self.browse3Btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.shape3Group)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.field3Combo = QtGui.QComboBox(self.shape3Group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.field3Combo.sizePolicy().hasHeightForWidth())
        self.field3Combo.setSizePolicy(sizePolicy)
        self.field3Combo.setObjectName(_fromUtf8("field3Combo"))
        self.horizontalLayout_5.addWidget(self.field3Combo)
        self.label_6 = QtGui.QLabel(self.shape3Group)
        self.label_6.setIndent(20)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_5.addWidget(self.label_6)
        self.prefix3Combo = QtGui.QComboBox(self.shape3Group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefix3Combo.sizePolicy().hasHeightForWidth())
        self.prefix3Combo.setSizePolicy(sizePolicy)
        self.prefix3Combo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.prefix3Combo.setObjectName(_fromUtf8("prefix3Combo"))
        self.prefix3Combo.addItem(_fromUtf8(""))
        self.prefix3Combo.addItem(_fromUtf8(""))
        self.prefix3Combo.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.prefix3Combo)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.shape3Group)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.confiniGroup = QtGui.QVBoxLayout()
        self.confiniGroup.setObjectName(_fromUtf8("confiniGroup"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_6.addWidget(self.label_10)
        self.filenameConfiniEdit = QtGui.QLineEdit(Dialog)
        self.filenameConfiniEdit.setObjectName(_fromUtf8("filenameConfiniEdit"))
        self.horizontalLayout_6.addWidget(self.filenameConfiniEdit)
        self.browseConfiniBtn = QtGui.QToolButton(Dialog)
        self.browseConfiniBtn.setObjectName(_fromUtf8("browseConfiniBtn"))
        self.horizontalLayout_6.addWidget(self.browseConfiniBtn)
        self.confiniGroup.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_12 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_7.addWidget(self.label_12)
        self.fieldComuneNameCombo = QtGui.QComboBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldComuneNameCombo.sizePolicy().hasHeightForWidth())
        self.fieldComuneNameCombo.setSizePolicy(sizePolicy)
        self.fieldComuneNameCombo.setObjectName(_fromUtf8("fieldComuneNameCombo"))
        self.horizontalLayout_7.addWidget(self.fieldComuneNameCombo)
        self.confiniGroup.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_8.addWidget(self.label_11)
        self.comuneNameCombo = QtGui.QComboBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comuneNameCombo.sizePolicy().hasHeightForWidth())
        self.comuneNameCombo.setSizePolicy(sizePolicy)
        self.comuneNameCombo.setObjectName(_fromUtf8("comuneNameCombo"))
        self.horizontalLayout_8.addWidget(self.comuneNameCombo)
        self.confiniGroup.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addLayout(self.confiniGroup)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Creazione database vuoto", None, QtGui.QApplication.UnicodeUTF8))
        self.shape1Group.setTitle(QtGui.QApplication.translate("Dialog", "Input shapefile #1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "Filename", None, QtGui.QApplication.UnicodeUTF8))
        self.browse1Btn.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Campo chiave univoca", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Prefisso", None, QtGui.QApplication.UnicodeUTF8))
        self.prefix1Combo.setItemText(0, QtGui.QApplication.translate("Dialog", "RT020101", None, QtGui.QApplication.UnicodeUTF8))
        self.prefix1Combo.setItemText(1, QtGui.QApplication.translate("Dialog", "RT020202", None, QtGui.QApplication.UnicodeUTF8))
        self.prefix1Combo.setItemText(2, QtGui.QApplication.translate("Dialog", "RT020107", None, QtGui.QApplication.UnicodeUTF8))
        self.shape2Group.setTitle(QtGui.QApplication.translate("Dialog", "Input shapefile #2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Filename", None, QtGui.QApplication.UnicodeUTF8))
        self.browse2Btn.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Campo chiave univoca", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Prefisso", None, QtGui.QApplication.UnicodeUTF8))
        self.prefix2Combo.setItemText(0, QtGui.QApplication.translate("Dialog", "RT020101", None, QtGui.QApplication.UnicodeUTF8))
        self.prefix2Combo.setItemText(1, QtGui.QApplication.translate("Dialog", "RT020202", None, QtGui.QApplication.UnicodeUTF8))
        self.prefix2Combo.setItemText(2, QtGui.QApplication.translate("Dialog", "RT020107", None, QtGui.QApplication.UnicodeUTF8))
        self.shape3Group.setTitle(QtGui.QApplication.translate("Dialog", "Input shapefile #3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Filename", None, QtGui.QApplication.UnicodeUTF8))
        self.browse3Btn.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Campo chiave univoca", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Prefisso", None, QtGui.QApplication.UnicodeUTF8))
        self.prefix3Combo.setItemText(0, QtGui.QApplication.translate("Dialog", "RT020101", None, QtGui.QApplication.UnicodeUTF8))
        self.prefix3Combo.setItemText(1, QtGui.QApplication.translate("Dialog", "RT020202", None, QtGui.QApplication.UnicodeUTF8))
        self.prefix3Combo.setItemText(2, QtGui.QApplication.translate("Dialog", "RT020107", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "Filename", None, QtGui.QApplication.UnicodeUTF8))
        self.browseConfiniBtn.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Dialog", "Colonna nomi municipi ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog", "Municipio", None, QtGui.QApplication.UnicodeUTF8))

