# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/wdgSezUnitaVolumetriche.ui'
#
# Created: Thu Jan 13 14:29:11 2011
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(589, 313)
        self.gridLayout_5 = QtGui.QGridLayout(Form)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 2, 0, 1, 1)
        self.INTERR_NPIANI = QtGui.QSpinBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INTERR_NPIANI.sizePolicy().hasHeightForWidth())
        self.INTERR_NPIANI.setSizePolicy(sizePolicy)
        self.INTERR_NPIANI.setObjectName("INTERR_NPIANI")
        self.gridLayout_5.addWidget(self.INTERR_NPIANI, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setIndent(40)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 2, 4, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 3, 0, 1, 2)
        self.ZZ_MORFOLOGIA_COPERTURAID = QtGui.QComboBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZZ_MORFOLOGIA_COPERTURAID.sizePolicy().hasHeightForWidth())
        self.ZZ_MORFOLOGIA_COPERTURAID.setSizePolicy(sizePolicy)
        self.ZZ_MORFOLOGIA_COPERTURAID.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.ZZ_MORFOLOGIA_COPERTURAID.setObjectName("ZZ_MORFOLOGIA_COPERTURAID")
        self.gridLayout_5.addWidget(self.ZZ_MORFOLOGIA_COPERTURAID, 3, 2, 1, 3)
        self.debugInfo = QtGui.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.debugInfo.setFont(font)
        self.debugInfo.setReadOnly(True)
        self.debugInfo.setObjectName("debugInfo")
        self.gridLayout_5.addWidget(self.debugInfo, 0, 0, 1, 5)
        self.FUORITERR_NPIANI = QtGui.QSpinBox(Form)
        self.FUORITERR_NPIANI.setObjectName("FUORITERR_NPIANI")
        self.gridLayout_5.addWidget(self.FUORITERR_NPIANI, 2, 3, 1, 1)
        self.SCHEDA_EDIFICIOID = QtGui.QLineEdit(Form)
        self.SCHEDA_EDIFICIOID.setObjectName("SCHEDA_EDIFICIOID")
        self.gridLayout_5.addWidget(self.SCHEDA_EDIFICIOID, 7, 0, 1, 5)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.MANTO_COPERTURA_UNITA_VOLUMETRICAID = WdgMantoCoperturaUnitaVolumetrica(self.tab)
        self.MANTO_COPERTURA_UNITA_VOLUMETRICAID.setObjectName("MANTO_COPERTURA_UNITA_VOLUMETRICAID")
        self.gridLayout_2.addWidget(self.MANTO_COPERTURA_UNITA_VOLUMETRICAID, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtGui.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.edificioOrdinarioRadio = QtGui.QRadioButton(self.tab_2)
        self.edificioOrdinarioRadio.setChecked(True)
        self.edificioOrdinarioRadio.setObjectName("edificioOrdinarioRadio")
        self.gridLayout.addWidget(self.edificioOrdinarioRadio, 0, 0, 1, 1)
        self.edificioGrandiLuciRadio = QtGui.QRadioButton(self.tab_2)
        self.edificioGrandiLuciRadio.setObjectName("edificioGrandiLuciRadio")
        self.gridLayout.addWidget(self.edificioGrandiLuciRadio, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.tipoEdificiStacked = QtGui.QStackedWidget(self.tab_2)
        self.tipoEdificiStacked.setObjectName("tipoEdificiStacked")
        self.STRUTTURE_ORIZZONTALI_COPERTURA_EDIFICI_ORDINARIID = WdgStruttureOrizzontaliCoperturaEdificiOrdinari()
        self.STRUTTURE_ORIZZONTALI_COPERTURA_EDIFICI_ORDINARIID.setObjectName("STRUTTURE_ORIZZONTALI_COPERTURA_EDIFICI_ORDINARIID")
        self.tipoEdificiStacked.addWidget(self.STRUTTURE_ORIZZONTALI_COPERTURA_EDIFICI_ORDINARIID)
        self.STRUTTURE_ORIZZONTALI_COPERTURA_EDIFICI_GRANDI_LUCIID = WdgStruttureOrizzontaliCoperturaEdificiGrandiLuci()
        self.STRUTTURE_ORIZZONTALI_COPERTURA_EDIFICI_GRANDI_LUCIID.setObjectName("STRUTTURE_ORIZZONTALI_COPERTURA_EDIFICI_GRANDI_LUCIID")
        self.tipoEdificiStacked.addWidget(self.STRUTTURE_ORIZZONTALI_COPERTURA_EDIFICI_GRANDI_LUCIID)
        self.gridLayout.addWidget(self.tipoEdificiStacked, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_5.addWidget(self.tabWidget, 5, 0, 1, 5)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 6, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem3, 4, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "N. piani interrati", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "N. piani fuori terra", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Morfologia della copertura", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Form", "Manto di copertura", None, QtGui.QApplication.UnicodeUTF8))
        self.edificioOrdinarioRadio.setText(QtGui.QApplication.translate("Form", "Edificio ordinario", None, QtGui.QApplication.UnicodeUTF8))
        self.edificioGrandiLuciRadio.setText(QtGui.QApplication.translate("Form", "Edificio con grandi luci (capannoni, palestre, piscine, etc.)", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Form", "Strutture orizzontali - Copertura", None, QtGui.QApplication.UnicodeUTF8))

from ..WdgStruttureOrizzontaliCoperturaEdificiOrdinari import WdgStruttureOrizzontaliCoperturaEdificiOrdinari
from ..WdgMantoCoperturaUnitaVolumetrica import WdgMantoCoperturaUnitaVolumetrica
from ..WdgStruttureOrizzontaliCoperturaEdificiGrandiLuci import WdgStruttureOrizzontaliCoperturaEdificiGrandiLuci
