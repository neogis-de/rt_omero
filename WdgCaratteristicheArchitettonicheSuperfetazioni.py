# -*- coding: utf-8 -*-

"""
/***************************************************************************
Name                 : Omero RT
Description          : Omero plugin
Date                 : August 15, 2010 
copyright            : (C) 2010 by Giuseppe Sucameli (Faunalia)
email                : sucameli@faunalia.it
 ***************************************************************************/

Omero plugin
Works done from Faunalia (http://www.faunalia.it) with funding from Regione 
Toscana - S.I.T.A. (http://www.regione.toscana.it/territorio/cartografia/index.html)

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from WdgCaratteristicheArchitettonicheChild import WdgCaratteristicheArchitettonicheChild

class WdgCaratteristicheArchitettonicheSuperfetazioni(WdgCaratteristicheArchitettonicheChild):

	def __init__(self, parent=None):
		multipleChoiseParams = ["ZZ_TIPO_SUPERFETAZIONI_SUPERFETAZIONI", "ZZ_TIPO_SUPERFETAZIONIID", "SUPERFETAZIONI_INCONGRUENZEID", "ZZ_TIPO_SUPERFETAZIONI"]
		WdgCaratteristicheArchitettonicheChild.__init__(self, parent, "SUPERFETAZIONI_INCONGRUENZE", None, multipleChoiseParams)
		self.showOtherInfos(False)

		# modifica il nome degli oggetti
		self.ZZ_TIPO.setObjectName("ZZ_TIPO_SUPERFETAZIONI_SUPERFETAZIONI")
		self.ALTRO.setObjectName("ALTRO_SUPERFETAZIONE_INCONGRUENZA")

	def getNomeCaratteristica(self):
		return "Superfetazioni e incongruenze"

