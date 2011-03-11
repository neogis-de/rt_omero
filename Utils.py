# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
import qgis.gui


class MapTool(QObject):
	canvas = None

	def __init__(self, mapToolClass, canvas=None):
		QObject.__init__(self)
		if canvas == None:
			if MapTool.canvas == None:
				raise Exception( "MapTool.canvas is None" )
			else:
				self.canvas = MapTool.canvas
		else:
			self.canvas = canvas
			if MapTool.canvas == None:
				MapTool.canvas = canvas

		self.tool = mapToolClass( self.canvas )
		QObject.connect(self.tool, SIGNAL( "geometryDrawingEnded" ), self.onEnd)

	def onEnd(self, geometry):
		self.stopCapture()
		if geometry == None:
			return
		self.emit( SIGNAL( "geometryEmitted" ), geometry )

	def isActive(self):
		return self.canvas != None and self.canvas.mapTool() == self.tool

	def startCapture(self):
		self.canvas.setMapTool( self.tool )

	def stopCapture(self):
		self.canvas.unsetMapTool( self.tool )

	class Drawer(qgis.gui.QgsMapToolEmitPoint):
		def __init__(self, canvas, isPolygon=False):
			self.canvas = canvas
			self.isPolygon = isPolygon
			qgis.gui.QgsMapToolEmitPoint.__init__(self, self.canvas)

			self.rubberBand = qgis.gui.QgsRubberBand( self.canvas, self.isPolygon )
			self.rubberBand.setColor( Qt.red )
			self.rubberBand.setWidth( 1 )

			self.snapper = qgis.gui.QgsMapCanvasSnapper( self.canvas )

			self.isEmittingPoints = False

		def reset(self):
			self.isEmittingPoints = False
			self.rubberBand.reset( self.isPolygon )

		def canvasPressEvent(self, e):
			if e.button() == Qt.RightButton:
				self.isEmittingPoints = False
				self.emit( SIGNAL("geometryDrawingEnded"), self.geometry() )
				return

			if e.button() == Qt.LeftButton:
				self.isEmittingPoints = True
			else:
				return
			point = self.toMapCoordinates( e.pos() )
			self.rubberBand.addPoint( point, True )	# true to update canvas
			self.rubberBand.show()

		def canvasMoveEvent(self, e):
			if not self.isEmittingPoints:
				return

			retval, snapResults = self.snapper.snapToBackgroundLayers( e.pos() )
			if retval == 0 and len(snapResults) > 0:
				point = snapResults[0].snappedVertex
			else:
				point = self.toMapCoordinates( e.pos() )

			self.rubberBand.movePoint( point )

		def isValid(self):
			return self.rubberBand.numberOfVertices() > 0

		def geometry(self):
			if not self.isValid():
				return None
			geom = self.rubberBand.asGeometry()
			if geom == None:
				return
			return QgsGeometry.fromWkt( geom.exportToWkt() )

		def deactivate(self):
			qgis.gui.QgsMapTool.deactivate(self)
			self.reset()
			self.emit(SIGNAL("deactivated()"))


class FeatureFinder(MapTool):

	def __init__(self, canvas=None):
		MapTool.__init__(self, qgis.gui.QgsMapToolEmitPoint, canvas=canvas)
		QObject.connect(self.tool, SIGNAL( "canvasClicked(const QgsPoint &, Qt::MouseButton)" ), self.onEnd)

	def onEnd(self, point, button):
		self.stopCapture()
		self.emit( SIGNAL("pointEmitted"), point, button )

	@classmethod
	def findAtPoint(self, layer, point, onlyTheClosestOne=True, onlyIds=False):
		QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

		# recupera il valore del raggio di ricerca
		settings = QSettings()
		(radius, ok) = settings.value( "/Map/identifyRadius", QGis.DEFAULT_IDENTIFY_RADIUS ).toDouble()
		if not ok or radius <= 0:
			radius = QGis.DEFAULT_IDENTIFY_RADIUS
		radius = MapTool.canvas.extent().width() * radius/100

		# crea il rettangolo da usare per la ricerca
		rect = QgsRectangle()
		rect.setXMinimum(point.x() - radius)
		rect.setXMaximum(point.x() + radius)
		rect.setYMinimum(point.y() - radius)
		rect.setYMaximum(point.y() + radius)
		rect = MapTool.canvas.mapRenderer().mapToLayerCoordinates(layer, rect)

		# recupera le feature che intersecano il rettangolo
		layer.select([], rect, True, True)

		ret = None

		if onlyTheClosestOne:
			minDist = -1
			featureId = None
			rect = QgsGeometry.fromRect(rect)
			count = 0

			f = QgsFeature()
			while layer.nextFeature(f):
				if onlyTheClosestOne:
					geom = f.geometry()
					distance = geom.distance(rect)
					if minDist < 0 or distance < minDist:
						minDist = distance
						featureId = f.id()

			if onlyIds:
				ret = featureId
			elif featureId != None:
				layer.featureAtId(featureId, f, True, True)
				ret = f

		else:
			IDs = []
			f = QgsFeature()
			while layer.nextFeature(f):
				IDs.append( f.id() )

			if onlyIds:
				ret = IDs
			else:
				ret = []
				for featureId in IDs:
					layer.featureAtId(featureId, f, True, True)
					ret.append( f )

		QApplication.restoreOverrideCursor()
		return ret
				

class PolygonDrawer(MapTool):

	class PolygonDrawer(MapTool.Drawer):
		def __init__(self, canvas):
			MapTool.Drawer.__init__(self, canvas, True)

	def __init__(self, canvas=None):
		MapTool.__init__(self, self.PolygonDrawer, canvas)

class LineDrawer(MapTool):

	class LineDrawer(MapTool.Drawer):
		def __init__(self, canvas):
			MapTool.Drawer.__init__(self, canvas, False)

	def __init__(self, canvas=None):
		MapTool.__init__(self, self.LineDrawer, canvas)


class PicViewer(QGraphicsView):
	def __init__(self, parent):
		QGraphicsView.__init__(self, parent)

	def loadImage(self, image):
		self.resetTransform()	# restore the original scale
		scene = self.scene()
		if scene == None:
			scene = PicViewer.Scene()
			self.connect( scene, SIGNAL( "openPicRequested" ), SIGNAL( "openPicRequested" ) )
			self.setScene( scene )

		scene.clear()

		from AutomagicallyUpdater import AutomagicallyUpdater
		value = AutomagicallyUpdater._getRealValue( image )
		if value == None:
			return

		item = PicViewer.Picture( value, self.size() )
		scene.addItem( item )

		#itemRect = item.boundingRect()
		#scale = min( self.width()/itemRect.width(), self.height()/itemRect.height() )
		#self.scale( scale, scale )
		#self.centerOn( item )


	def getBytes(self, itemIndex=0):
		if self.scene() == None:
			return
		items = self.scene().items()
		if len(items) <= 0 or itemIndex >= len(items):
			return
		return items[itemIndex].getBytes()

	def clearCache(self, itemIndex=0):
		if self.scene() == None:
			return
		items = self.scene().items()
		if len(items) <= 0:
			return
		items[itemIndex].clearCache()

	class Scene(QGraphicsScene):
		def __init__(self, *argv):
			QGraphicsScene.__init__(self, *argv)

		def mouseDoubleClickEvent(self, event):
			if event.button() != Qt.LeftButton:
				return
			self.emit( SIGNAL( "openPicRequested" ) )
			QGraphicsScene.mouseDoubleClickEvent(self, event)

	class Picture(QGraphicsPixmapItem):
		def __init__(self, image, newSize=QSize(), parent=None):
			self.clearCache()

			pixmap = QPixmap()
			if isinstance(image, str) or isinstance(image, QString):
				infile = open( unicode(image).encode('utf8'), "rb" )
				self.imageBytes = QByteArray( infile.read() )
				infile.close()
				pixmap = QPixmap( image )

			elif isinstance(image, QByteArray):
				self.imageBytes = image
				pixmap.loadFromData( self.imageBytes )

			if newSize.isValid():
				pixmap = pixmap.scaled( newSize.width(), newSize.height(), Qt.KeepAspectRatio )

			QGraphicsPixmapItem.__init__(self, pixmap, parent)

		def getBytes(self):
			return self.imageBytes

		def clearCache(self):
			self.imageBytes = None


class TemporaryFile:
	# gestisci i file temporanei, eliminandoli alla chiusura del plugin
	tmpFiles = {}

	@staticmethod
	def getNewFile(key=None):
		tmp = QTemporaryFile()
		if not TemporaryFile.tmpFiles.has_key( key ):
			TemporaryFile.tmpFiles[ key ] = [ tmp ]
		else:
			TemporaryFile.tmpFiles[ key ].append( tmp )
		return tmp

	@staticmethod
	def delFile(tmp, key=None):
		if not TemporaryFile.tmpFiles.has_key( key ):
			return False
		if tmp != None:	# rimuovi solo il file passato
			if TemporaryFile.tmpFiles[ key ].count( tmp ) > 0:
				TemporaryFile.tmpFiles[ key ].remove( tmp )
				del tmp
		else:	# rimuovi tutti i file che hanno quella chiave
			for tmp in TemporaryFile.tmpFiles[ key ]:
				TemporaryFile.tmpFiles[ key ].remove( tmp )
				del tmp
			del TemporaryFile.tmpFiles[ key ]
		return True

	@staticmethod
	def delAllFiles(key=None):
		return TemporaryFile.delFile(None, key)

	@staticmethod
	def clear():
		for key, tmpList in TemporaryFile.tmpFiles.iteritems():
			for tmp in tmpList:
				TemporaryFile.tmpFiles[ key ].remove( tmp )
				del tmp
			del tmpList
		TemporaryFile.tmpFiles = {}

