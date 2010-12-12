# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/wdgSezLocalizzazione.ui'
#
# Created: Wed Nov 24 15:49:42 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(532, 181)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.EDIFICIO_ISOLATO = QtGui.QCheckBox(Form)
        self.EDIFICIO_ISOLATO.setObjectName("EDIFICIO_ISOLATO")
        self.gridLayout.addWidget(self.EDIFICIO_ISOLATO, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.NUM_UNITA_IMMOBILIARI = QtGui.QSpinBox(Form)
        self.NUM_UNITA_IMMOBILIARI.setMinimum(1)
        self.NUM_UNITA_IMMOBILIARI.setObjectName("NUM_UNITA_IMMOBILIARI")
        self.gridLayout.addWidget(self.NUM_UNITA_IMMOBILIARI, 2, 1, 1, 2)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.ZZ_PROPRIETA_PREVALENTEID = QtGui.QComboBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZZ_PROPRIETA_PREVALENTEID.sizePolicy().hasHeightForWidth())
        self.ZZ_PROPRIETA_PREVALENTEID.setSizePolicy(sizePolicy)
        self.ZZ_PROPRIETA_PREVALENTEID.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.ZZ_PROPRIETA_PREVALENTEID.setObjectName("ZZ_PROPRIETA_PREVALENTEID")
        self.gridLayout.addWidget(self.ZZ_PROPRIETA_PREVALENTEID, 3, 1, 1, 2)
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.PARTICELLE_CATASTALI = WdgParticelleCatastali(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PARTICELLE_CATASTALI.sizePolicy().hasHeightForWidth())
        self.PARTICELLE_CATASTALI.setSizePolicy(sizePolicy)
        self.PARTICELLE_CATASTALI.setObjectName("PARTICELLE_CATASTALI")
        self.gridLayout.addWidget(self.PARTICELLE_CATASTALI, 4, 1, 1, 2)
        self.ZZ_POSIZIONE_EDIFICIO_AGGREGATOID = QtGui.QComboBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZZ_POSIZIONE_EDIFICIO_AGGREGATOID.sizePolicy().hasHeightForWidth())
        self.ZZ_POSIZIONE_EDIFICIO_AGGREGATOID.setSizePolicy(sizePolicy)
        self.ZZ_POSIZIONE_EDIFICIO_AGGREGATOID.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.ZZ_POSIZIONE_EDIFICIO_AGGREGATOID.setObjectName("ZZ_POSIZIONE_EDIFICIO_AGGREGATOID")
        self.gridLayout.addWidget(self.ZZ_POSIZIONE_EDIFICIO_AGGREGATOID, 1, 2, 1, 1)
        self.LOCALIZZAZIONE_EDIFICIO_INDIRIZZO_VIA = MultiTabLocalizzazioneIndirizzi(Form)
        self.LOCALIZZAZIONE_EDIFICIO_INDIRIZZO_VIA.setObjectName("LOCALIZZAZIONE_EDIFICIO_INDIRIZZO_VIA")
        self.gridLayout.addWidget(self.LOCALIZZAZIONE_EDIFICIO_INDIRIZZO_VIA, 5, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.EDIFICIO_ISOLATO.setText(QtGui.QApplication.translate("Form", "Edificio isolato", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Posizione dell\'edificio nell\'aggregato strutturale", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Num. unità immobiliari", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Proprietà prevalente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Particelle catastali", None, QtGui.QApplication.UnicodeUTF8))

from ..MultiTabLocalizzazioneIndirizzi import MultiTabLocalizzazioneIndirizzi
from ..WdgParticelleCatastali import WdgParticelleCatastali
