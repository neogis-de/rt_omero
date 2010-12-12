# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import qgis.gui
import qgis.core

from ui.wdgLocalizzazioneIndirizzi_ui import Ui_Form
from AutomagicallyUpdater import *

from ManagerWindow import ManagerWindow

class WdgLocalizzazioneIndirizzi(QWidget, MappingOne2One, Ui_Form):

	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
		MappingOne2One.__init__(self, "INDIRIZZO_VIA")
		self.setupUi(self)

		# mostra le vie che corrispondono all'input dell'utente
		self.VIA.completer().setCompletionMode(QCompleter.PopupCompletion)

		# carica i widget multivalore con i valori delle relative tabelle
		tablesDict = {
			self.ZZ_PROVINCEISTATPROV: AutomagicallyUpdater.ZZTable( "ZZ_PROVINCE", "ISTATPROV", "NOME" )
		}
		self.setupTablesUpdater(tablesDict)
		self.loadTables()

		# mappa i widget con i campi delle tabelle
		childrenList = [
			self.ZZ_COMUNIISTATCOM, 
			self.VIA
		]
		self.setupValuesUpdater(childrenList)

		self.connect(self.ZZ_PROVINCEISTATPROV, SIGNAL("currentIndexChanged(int)"), self.caricaComuni)
		self.connect(self.ZZ_COMUNIISTATCOM, SIGNAL("currentIndexChanged(int)"), self.caricaVie)
		self.connect(self.VIA, SIGNAL("editTextChanged(const QString &)"), self.caricaCivici)
		self.connect(self.NUMERI_CIVICI, SIGNAL( "dataChanged()" ), self.aggiornaTitoloScheda)

		self.caricaComuni()
		self.caricaVie()


	def caricaComuni(self):
		self.ZZ_COMUNIISTATCOM.clear()
		self.ZZ_COMUNIISTATCOM.setCurrentIndex(-1)

		provincia = self.getValue(self.ZZ_PROVINCEISTATPROV)
		self.ZZ_COMUNIISTATCOM.setEnabled( provincia != None )

		# aggiorna la visualizzazione
		self.setValue(self.ZZ_COMUNIISTATCOM, None)

		if provincia == None:
			return

		# carica i comuni della provincia selezionata
		self.loadTables( self.ZZ_COMUNIISTATCOM, AutomagicallyUpdater.Query( "SELECT ISTATCOM, NOME FROM ZZ_COMUNI WHERE ZZ_PROVINCEISTATPROV = ? ORDER BY NOME ASC", [provincia] ) )

	def caricaVie(self):
		self.VIA.clear()
		self.VIA.setCurrentIndex(-1)

		comune = self.getValue(self.ZZ_COMUNIISTATCOM)
		self.VIA.setEnabled( comune != None )

		# aggiorna la visualizzazione
		self.setValue(self.VIA, None)

		if comune == None:
			return

		# carica le vie del comune selezionato
		self.loadTables( self.VIA, AutomagicallyUpdater.Query( "SELECT ID_INDIRIZZO, VIA, upper(VIA) AS VIAORDERED FROM INDIRIZZO_VIA WHERE ZZ_COMUNIISTATCOM = ? ORDER BY VIAORDERED ASC", [comune] ) )


	def caricaCivici(self):
		self.NUMERI_CIVICI.clear()

		via = self.getValue(self.VIA)
		self.NUMERI_CIVICI.setEnabled( via != None )

		# aggiorna la visualizzazione
		self.setValue(self.NUMERI_CIVICI, None)

		# carica i civici dell'indirizzo selezionato
		self.NUMERI_CIVICI.loadValues( AutomagicallyUpdater.Query( "SELECT IDNUMEROCIVICO, N_CIVICO, MOD_CIVICO FROM NUMERI_CIVICI WHERE INDIRIZZO_VIAID_INDIRIZZO = ?", [via] ) )

	def aggiornaTitoloScheda(self):
		provincia = self.ZZ_PROVINCEISTATPROV.currentText()
		comune = self.ZZ_COMUNIISTATCOM.currentText()
		via = self.VIA.currentText()
		civico = self.NUMERI_CIVICI.rowToString()

		indirizzo = "%s, %s - %s (%s)" % (via, civico, comune, provincia)
		self.emit( SIGNAL("indirizzoChanged(const QString &)"), indirizzo )

	# gestisti a parte il caso del widget VIA così da effettuare un test CaseInsensitive
	def getValue(self, widget):
		if self._getRealWidget(widget) != self.VIA:
			return AutomagicallyUpdater.getValue(widget)

		value = AutomagicallyUpdater.getValue(widget)
		if value != None:
			index = self.VIA.findData( value )
			if index >= 0:
				return value

		index = self.VIA.findText( value if value != None else QString(), Qt.MatchFixedString )
		if index >= 0:
			ID = self._getRealValue( self.VIA.itemData(index).toString() )
			if ID != None:
				return ID

		return value

	# impostando il comune bisogna aggiornare anche la provincia
	def setValue(self, widget, value):
		value = self._getRealValue(value)
		if self._getRealWidget(widget) != self.ZZ_COMUNIISTATCOM or value == None:
			return AutomagicallyUpdater.setValue(widget, value)

		query = AutomagicallyUpdater.Query("SELECT ZZ_PROVINCEISTATPROV FROM ZZ_COMUNI WHERE ISTATCOM = ?", [value])

		self.disconnect(self.ZZ_PROVINCEISTATPROV, SIGNAL("currentIndexChanged(int)"), self.caricaComuni)
		self.setValue(self.ZZ_PROVINCEISTATPROV, query)
		self.caricaComuni()
		self.connect(self.ZZ_PROVINCEISTATPROV, SIGNAL("currentIndexChanged(int)"), self.caricaComuni)
		
		AutomagicallyUpdater.setValue(self.ZZ_COMUNIISTATCOM, value)


	def getComuneVia(self):
		return ( self.getValue(self.ZZ_COMUNIISTATCOM), self.getValue(self.VIA) )

	def setComuneVia(self, comune, via):
		#self.disconnect(self.ZZ_COMUNIISTATCOM, SIGNAL("currentIndexChanged(int)"), self.caricaVie)
		self.setValue(self.ZZ_COMUNIISTATCOM, comune)
		#self.caricaVie()
		#self.connect(self.ZZ_COMUNIISTATCOM, SIGNAL("currentIndexChanged(int)"), self.caricaVie)

		self.setValue(self.VIA, via)


	def setupLoader(self, ID=None):
		MappingOne2One.setupLoader(self, ID)
		IDLocalizzazione = self._parentRef._ID
		self.NUMERI_CIVICI.setupLoader([IDLocalizzazione, ID])

	def delete(self):
		if self._ID == None:
			return

		# elimina dalla tabella di normalizzazione
		filters = {
			self._parentRef._parentPkColumn : self._parentRef._ID, 
			self._parentRef._pkColumn : self._ID
		}
		self._deleteValue(self._parentRef._tableName, filters)

		# elimina solo se non sono presenti altri riferimenti a questo oggetto
		query = AutomagicallyUpdater.Query( "SELECT count(*) FROM %s WHERE %s = ?" % (self._parentRef._tableName, self._parentRef._pkColumn), [self._ID] )
		query = query.getQuery()
		if query == None:
			return
		if not query.exec_() or not query.next():
			return

		if query.value(0).toInt()[0] <= 1:
			# elimina l'indirizzo dalla tabella
			MappingOne2One.delete(self)

			#elimina i numeri civici
			self.NUMERI_CIVICI.delete()


	def save(self):
		ID = None

		values = {}
		for widget in self._recursiveChildrenRefs():
			if not ( isinstance(widget, MappingOne2Many) or isinstance(widget, MappingMany2Many) ):
				value = self.getValue(widget)
				if widget == self.VIA:
					# non salvare duplicati: controlla che non esista già nella combo
					if value != None:
						index = self.VIA.findData( value )
						if index >= 0:
							ID = value
							break
					else:
						value = ''

				values[widget.objectName()] = value

		if ID == None:
			ID = self._saveValue(values, self._tableName, self._pkColumn, self._ID)
			if ID == None:
				return False
		self._ID = ID

		IDLocalizzazione = self._parentRef._ID
		self.NUMERI_CIVICI._ID = [IDLocalizzazione, self._ID]
		self.NUMERI_CIVICI.save()

		return True
