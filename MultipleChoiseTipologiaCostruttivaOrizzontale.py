# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import qgis.gui
import qgis.core

from MultipleChoise2Lists import MultipleChoise2Lists
from AutomagicallyUpdater import *

class MultipleChoiseTipologiaCostruttivaOrizzontale(MultipleChoise2Lists):

	def __init__(self, parent=None):
		MultipleChoise2Lists.__init__(self, parent, "TIPOLOGIA_COSTRUTTIVA_ORIZZONTALE_PREVALENTE_STRUTTURE_ORIZZONTALI_SOLAI", None, "STRUTTURE_ORIZZONTALI_SOLAIID", "ZZ_TIPOLOGIA_COSTRUTTIVA_ORIZZONTALE_PREVALENTE")

