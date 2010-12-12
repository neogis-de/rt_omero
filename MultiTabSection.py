# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import qgis.gui
import qgis.core

from ui.multiTabSection_ui import Ui_MultiTabSection
from AutomagicallyUpdater import *

class MultiTabSection(QWidget, MappingOne2Many, Ui_MultiTabSection):

	def __init__(self, parent=None, basePageWidget=QWidget, baseTabName="Tab ", table=None, pk=None, parentPk=None):
		QWidget.__init__(self, parent)
		MappingOne2Many.__init__(self, table, pk, parentPk)
		self.setupUi(self)

		self.baseTabName = baseTabName
		self.basePageWidget = basePageWidget

		self.clear()

		self.connect(self.tabWidget, SIGNAL( "currentChanged(int)" ), self.aggiornaPulsanti)
		self.connect(self.btnDelete, SIGNAL( "clicked()" ), self.btnDeleteTabClicked)
		self.connect(self.btnNew, SIGNAL( "clicked()" ), self.btnAddTabClicked)

		self.aggiornaPulsanti()

	def clear(self):
		for i in range(self.tabWidget.count()-1, -1, -1):
			w = self.tabWidget.widget(i)
			self.tabWidget.removeTab(i)
			del w

		self.tabWidget.clear()
		first = self.addTab()
		

	def aggiornaPulsanti(self):
		self.btnDelete.setEnabled(self.tabWidget.currentIndex() > 0)


	def btnDeleteTabClicked(self):
		self.deleteTab()

	def deleteTab(self):
		index = self.tabWidget.currentIndex()
		if index <= 0:
			return

		widget = self.tabWidget.widget(index)
		ret = widget.delete() # elimina dal db
		self.delChildRef(widget)	# elimina il riferimento
		self.tabWidget.removeTab(index)
		del widget
		
		for i in range(1, self.tabWidget.count()):
			text = "%s%d" % (self.baseTabName, i+1)
			self.tabWidget.setTabText(i, QString(text) )
		return ret

	def btnAddTabClicked(self):
		index = self.addTab()
		self.tabWidget.setCurrentIndex(index)

	def addTab(self):
		index = self.tabWidget.addTab(self.basePageWidget(), QString())
		text = "%s%d" % (self.baseTabName, index+1)
		self.tabWidget.setTabText(index, QString(text) )
		self.addChildRef(self.tabWidget.widget(index))
		return index

	def setBaseTabName(self, name):
		self.baseTabName = name

	def setBasePageWidget(self, widget):
		self.basePageWidget = widget

	def setBaseTab(self, widget, name):
		self.setBasePageWidget(widget)
		self.setBaseTabName(name)


	def addNewChild(self):
		self.addTab()
		return True

	def setupUpdater(self, ID=None):
		MappingOne2Many.setupUpdater(ID)
		self.tabWidget.setCurrentIndex(0)
