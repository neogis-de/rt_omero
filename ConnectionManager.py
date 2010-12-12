# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtSql import *
from pyspatialite import dbapi2 as sqlite

class ConnectionManager:

	defaultConnType = "QSQLITE"
	defaultConnName = "rt_omero_default_connection"

	connPySL = None
	isTransaction = False
	transactionError = False
	numTransaction = 0

	@classmethod
	def setConnection(self, path):
		# connessione tramite pyspatialite
		try:
			self.connPySL = PySLDatabase(path)
		except sqlite.OperationalError, e:
			return False

		# connessione tramite QtSql
		conn = QSqlDatabase.database( self.defaultConnName )
		if conn.isValid():
			return True

		conn = QSqlDatabase.addDatabase( self.defaultConnType, self.defaultConnName )
		conn.setHostName("localhost")
		conn.setDatabaseName(path)
		return conn.open()

	@classmethod
	def closeConnection(self):
		self.connPySL = None

		conn = QSqlDatabase.database( self.defaultConnName )
		if conn.isValid():
			QSqlDatabase.removeDatabase( self.defaultConnName )

	@classmethod
	def getConnection(self, type=0):
		if type == 1:
			conn = self.connPySL
		else:
			conn = QSqlDatabase.database( self.defaultConnName, True )

		if not conn.isValid():
			return None
		return conn

	@classmethod
	def getNewQuery(self, type=0):
		conn = self.getConnection(type)
		if conn == None:
			return None

		if self.isTransaction and self.transactionError:
			return None

		if type == 1:
			return PySLQuery(conn, not self.isTransaction)
		return QSqlQuery(conn)

	@classmethod
	def startTransaction(self):
		self.transactionError = False
		conn = self.getConnection(0)
		self.isTransaction = conn != None and conn.transaction()
		conn = self.getConnection(1)
		self.isTransaction = self.isTransaction and conn != None and conn.transaction()
		self.numTransaction = self.numTransaction + 1
		if self.numTransaction == 1:
			from AutomagicallyUpdater import AutomagicallyUpdater
			AutomagicallyUpdater._setEditFlag( True )
		return self.isTransaction

	@classmethod
	def abortTransaction(self, errorMsg=QString()):
		if not self.isTransaction:
			return
		self.transactionError = True

		conn = self.getConnection(0)
		if conn != None:
			conn.rollback()

		conn = self.getConnection(1)
		if conn != None:
			conn.rollback()

		raise ConnectionManager.AbortedException( errorMsg )

	@classmethod
	def endTransaction(self, force=False):
		if not self.isTransaction:
			return
		self.isTransaction = False
		self.numTransaction = self.numTransaction - 1 

		if self.numTransaction > 0 and not force:
			return

		from AutomagicallyUpdater import AutomagicallyUpdater
		AutomagicallyUpdater._setEditFlag( False )

		if self.transactionError:
			self.transactionError = False
			return

		conn = self.getConnection(0)
		if conn != None:
			conn.commit()

		conn = self.getConnection(1)
		if conn != None:
			conn.commit()


	class AbortedException(Exception):
		def __init__(self, msg):
			self.msg = QString(msg)
			Exception(self, self.msg)

		def toString(self):
			return self.msg


class PySLDatabase:

	def __init__(self, path):
		self._error = QString()
		try:
			self.connection = sqlite.connect(u"%s" % path)
		except sqlite.OperationalError, e:
			self._error = QString( str(e) )

	def getQuery(self, autocommit=True):
		return PySLQuery(self)

	def __del__(self):
		if self.connection != None:
			del self.connection

	def isValid(self):
		return self._error.isEmpty()

	def transaction(self):
		return True

	def rollback(self):
		self.connection.rollback()

	def commit(self):
		self.connection.commit()

class PySLError:
	def __init__(self, msg=''):
		self.msg = QString(msg)

	def text(self):
		return self.msg

class PySLQuery:

	def __init__(self, conn, autocommit=True):
		self._autocommit = autocommit
		self._dbconn = conn
		self._cursor = self._dbconn.connection.cursor()
		self.clear()

	def clear(self):
		self._sql = QString()
		self._query = QString()
		self._params = []
		self._error = PySLError()
		self._value = None

	def prepare(self, sql):
		self.setQuery(sql)

	def escapeValue(self, value):
		if value == None:
			return 'NULL'
		if isinstance(value, QVariant):
			if not value.isValid():
				return 'NULL'
			value = value.toString()
		if isinstance(value, QByteArray):
			return buffer(value)
		return "%s" % value

	def convertResult(self, value):
		return QVariant(value) if value != None else QVariant()

	def addBindValue(self, value):
		self._params.append( self.escapeValue(value) )

	def setQuery(self, sql):
		self.clear()
		self._sql = QString(sql)
		self._query = self._sql

	def exec_(self, sql=None):
		if sql != None:
			self.setQuery(sql)

		try:
			self._cursor.execute(u"%s" % self._query, self._params)
		except sqlite.Error, e:
			self._error = PySLError( str(e) )
			return False

		return True

	def lastQuery(self):
		return QString(self._sql)

	def lastError(self):
		return self._error

	def next(self):
		self._value = self._cursor.fetchone()
		return self._value != None

	def value(self, index):
		if index < len(self._value):
			val = self._value[index]
			return QVariant(val) if val != None else QVariant()
		return None

	def lastInsertId(self):
		return self.convertResult(self._cursor.lastrowid)

	def rollback(self):
		self._dbconn.rollback()

	def commit(self):
		self._dbconn.commit()

	def __del__(self):
		if self._autocommit:
			self.commit()

