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
	'''Lista de extenciones vacia'''
	def __init__(self):
		self.name = "Null"

	def imprimir(self):
		print "Lista de extenciones Null"

class CuerpoClaseAtributo(Nodo):
	'''Declaracion de los atributos de la clase'''
	def __init__(self, atributos):
		self.name      = "atributos"
		self.atributos = atributos

	def imprimir(self):
		print 'Atributos'
		self.atributos.imprimir()

class CuerpoClaseMetodo(Nodo):
	'''Declaracion de los metodos de la clase'''
	def __init__(self, metodos):
		self.name      = "metodos"
		self.metodos = metodos

	def imprimir(self):
		print 'Metodos'
		self.metodos.imprimir()

class CuerpoClaseNull(Nodo):
	'''declaracion del cuerpo de las clases'''
	def __init__(self):
		self.name = "Null"

	def imprimir(self):
		print "Cuerpo de la clase Null"

class DeclaracionAtributos(Nodo):
	'''Declaracion de lista de atributos'''
	def  __init__(self, atributos, tipo, name):
		self.name 	   = name
		self.tipo      = tipo
		self.atributos = atributos

	def imprimir(self):
		print "Lista de atributos"
		self.tipo.imprimir()
		self.atributos.imprimir()

class DeclaracionAtributo(Nodo):
	'''Declaracion de atributo'''
	def  __init__(self, tipo, name):
		self.name 	   = name
		self.tipo      = tipo

	def imprimir(self):
		print "Atributo"
		self.tipo.imprimir()
		self.name.imprimir()

class DeclaracionAtributoNull(Nodo):
	'''Declaracion vacia de atributos'''
	def  __init__(self):
		self.name 	   = "Null"

	def imprimir(self):
		print "Declaracion de atributos vacia"

class DeclaracionMetodos(Nodo):
	'''Declaracion de metodos'''
	def __init__(self, tipo, identificador, argumentos, cuerpo):
		self.nombre = identificador
		self.tipo   = tipo
		self.argumentos = argumentos
		self.cuerpo 	= cuerpo

	def imprimir(self):
		print "metodo "+self.nombre


class DeclaracionMetodosNull(Nodo):
	'''Declaracion vacia de metodos'''
	def __init__(self):
		self.name = "Null"

	def imprimir(self):
		print "Declaracion vacia de metodos"


class Argumentos(Nodo):
	'''Declaracion de argumentos de metodos'''
	def __init__(self, argumentos, tipo, identificador):
		self.name 		= identificador
		self.tipo 		= tipo
		self.argumentos = argumentos

	def imprimir(self):
		print 'Argumentos del metodo '+self.identificador
		self.tipo.imprimir()
		self.argumentos.imprimir()

class Argumento(Nodo):
	'''Declaracion de un solo argumento'''
	def __init__(self, tipo, identificador):
		self.name = identificador
		self.tipo = tipo

	def imprimir(self):
		print "Argumento del metodo "+self.name
		self.tipo.imprimir()

class ArgumentosNull(Nodo):
	'''Declaracion vacia de argumentos'''
	def __init__(self):
		self.name = "Null"

	def imprimir(self):
		print "Declaracion vacia de argumentos"

class CuerpoMetodo(Nodo):
	'''Cuerpo del metodo'''
	def __init__(self, variable, sentencias):		
		self.name       = "cuerpo del metodo"
		self.variable   = variable
		self.sentencias = sentencias

	def imprimir(self):
		print "Cuerpo del metodo"
		self.variable.imprimir()
		self.sentencias,imprimir()

class CuerpoMetodoNull(Nodo):
	'''Cuerpo vacio del metodo'''
	def __init__(self):
		self.name = "Null"

	def imprimir(self):
		print "Cuerpo vacio del metodo"
		
		

class Type(Nodo):
	'''Tipos de datos'''
	def __init__(self, tipo):
		self.tipo = tipo
		self.name = "tipo"

	def imprimir(self):
		print "tipo"
		self.tipo.imprimir();

class TypeNull(Nodo):
	'''Tipo vacion'''
	def __init__(self):
		self.name = "Null"

	def imprimir(self):
		print "Tipo vacio"
