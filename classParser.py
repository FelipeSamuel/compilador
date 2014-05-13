class Nodo:
	'''docstring for Node'''
	pass

class Programa(Nodo):
	'''Programa se compone de una lista de declaraciones'''
	def __init__(self, listaDeclaraciones):
		self.listaDeclaraciones = listaDeclaraciones
		self.name               = "Programa"

	def imprimir(self):
		print 'axioma'
		self.listaDeclaraciones.imprimir()

class ListaDeclaracion(Nodo):
	"""Lista las declaraciones de clases dentro del codigo fuente"""
	def __init__(self, declaracionClase, listaDeclaraciones):
		self.declaracionClase   = declaracionClase
		self.listaDeclaraciones = listaDeclaraciones
		self.name               = "ListaDeclaracion"

	def imprimir(self):
		print 'Lista de declaraciones'
		self.declaracionClase.imprimir()
		self.listaDeclaraciones.imprimir()

class ListaDeclaracionNull(Nodo):
	'''Termina con la recursividad de la lista de declaraciones'''
	def __init__(self):
		self.name = "Null"

	def imprimir(self):
		print "Lista de declaraciones Null"

class DeclaracionClase(Nodo):
	'''Representacion de las clases'''
	def __init__(self, identificador, declaracionExtenciones, cuerpoClase):
		self.name                   = identificador
		self.declaracionExtenciones = declaracionExtenciones
		self.cuerpoClase            = cuerpoClase

	def imprimir(self):
		print "declaracion de la clase"
		self.declaracionExtenciones.imprimir()
		self.cuerpoClase.imprimir()

class Identificador(Nodo):
	'''Optiene el identificador o nombre de las clases, atributos, metodos, etc'''
	def __init__(self, name, lineno):
		self.name   = name
		self.lineno = lineno

	def imprimir(self):
		print "id"

class DeclaracionExtenciones(Nodo):
	'''Se declaran los extens del lenguaje'''
	def __init__(self, name):
		self.name = name

	def imprimir(self):
		print "declaracion de los extens"

class DeclaracionExtencionesNull(Nodo):
	"""docstring for DeclaracionExtencionesNull"""
	def __init__(self):		
		self.nombre = "Null"

	def imprimir():
		print "Lista de extenciones Null"
		
class CuerpoClaseNull(Nodo):
	'''declaracion del cuerpo de las clases'''
	def __init__(self):
		self.nombre = "Null"

	def imprimir():
		print "Cuerpo de la clase Null"

		



