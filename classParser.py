class Nodo:
	'''Nodo raiz'''
	pass

class Programa(Nodo):
	'''Programa se compone de una lista de declaraciones'''
	def __init__(self, ListaDeclaraciones):
		self.nombre               = "Programa"
		self.ListaDeclaraciones = ListaDeclaraciones

	def imprimir(self,espacio):
		print self.nombre
		self.ListaDeclaraciones.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vPrograma(self)

class ListaDeclaraciones(Nodo):
	"""Lista las declaraciones de clases dentro del codigo fuente"""
	def __init__(self, DeclaracionClase, ListaDeclaraciones):
		self.nombre 		    = "Declaracion de Clase"
		self.DeclaracionClase   = DeclaracionClase
		self.ListaDeclaraciones = ListaDeclaraciones

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.DeclaracionClase.imprimir(espacio+' ')
		self.ListaDeclaraciones.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vListaDeclaraciones(self)

class DeclaracionClase(Nodo):
	'''Representacion de las clases'''
	def __init__(self, nombre, DeclaracionExtenciones, CuerpoClase):
		self.nombre 				= nombre
		self.DeclaracionExtenciones = DeclaracionExtenciones
		self.CuerpoClase            =CuerpoClase

	def imprimir(self,espacio):
		print espacio+"Clase "+self.nombre
		self.DeclaracionExtenciones.imprimir(espacio+' ')
		self.CuerpoClase.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vDeclaracionClase(self)

class DeclaracionExtenciones(Nodo):
	'''Se declaran los extens del lenguaje'''
	def __init__(self, nombre):
		self.nombre = 'extencion '+nombre

	def imprimir(self,espacio):
		print espacio+self.nombre

	def aceptar(self, visitante):
		return visitante.vDeclaracionExtenciones(self)

class CuerpoClase(Nodo):
	'''Declaracion del Cuerpo de una clase'''
	def __init__(self, ListaCuerpoClase, CuerpoClase):
		self.nombre           = "Cuerpo Clase"
		self.ListaCuerpoClase = ListaCuerpoClase
		self.CuerpoClase      = CuerpoClase

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.ListaCuerpoClase.imprimir(espacio+' ')
		self.CuerpoClase.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vCuerpoClase(self)


class CuerpoClaseAtributos(Nodo):

	def __init__(self, DeclaracionAtributos):
		self.nombre               = 'Declaracion Atributos'
		self.DeclaracionAtributos = DeclaracionAtributos

	def imprimir(self, espacio):
		print espacio+self.nombre
		self.DeclaracionAtributos.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vCuerpoClaseAtributos(self)

class CuerpoClaseMetodos(Nodo):

	def __init__(self, DeclaracionMetodos):
		self.nombre             = 'Declaracion Metodos'
		self.DeclaracionMetodos = DeclaracionMetodos

	def imprimir(self, espacio):
		print espacio+self.nombre
		self.DeclaracionMetodos.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vCuerpoClaseMetodos(self)


class ListaAtribMetod(Nodo):
	def __init__(self, Declaraciones):
		self.nombre    = "cuerpo clase"
		self.Declaraciones = Declaraciones

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.Declaraciones.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vListaAtribMetod(self)

class DeclaracionAtributos(Nodo):
	def __init__(self, nombre, ListaAtributos,DeclaracionAtributos):
		self.nombre 			  = nombre
		self.ListaAtributos 	  = ListaAtributos
		self.DeclaracionAtributos = DeclaracionAtributos

	def imprimir(self,espacio):
		print espacio+"Atributo "+self.nombre
		self.ListaAtributos.imprimir(espacio+' ')
		self.DeclaracionAtributos.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vDeclaracionAtributos(self)

class ListaAtributos(Nodo):
	def __init__(self, nombre, ListaAtributos):
		self.nombre 		= "Atributo "+nombre
		self.ListaAtributos = ListaAtributos

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.ListaAtributos.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vListaAtributos(self)

class DeclaracionMetodos(Nodo):

	def __init__(self, TipoRetorno,nombre,Argumetos,CuerpoMetodo):
		self.nombre       = "Metodo "+nombre
		self.TipoRetorno  = TipoRetorno
		self.Argumetos 	  = Argumetos
		self.CuerpoMetodo = CuerpoMetodo

	def imprimir(self,espacio):
		print espacio+self.nombre
		#self.TipoRetorno.imprimir(espacio+' ')
		self.Argumetos.imprimir(espacio+' ')
		self.CuerpoMetodo.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vDeclaracionMetodos(self)

class DeclaracionMetodosVoid(Nodo):

	def __init__(self, TipoRetorno,nombre,Argumetos,CuerpoMetodo):
		self.nombre       = nombre
		self.TipoRetorno  = TipoRetorno
		self.Argumetos 	  = Argumetos
		self.CuerpoMetodo = CuerpoMetodo

	def imprimir(self,espacio):
		print espacio+"Metodo "+self.nombre
		print espacio+self.TipoRetorno
		self.Argumetos.imprimir(espacio+' ')
		self.CuerpoMetodo.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vDeclaracionMetodosVoid(self)

"""clad(Nodo):

	def __init__(self, Retorno):
		self.nombre  = "Retorno del Metodo"
		self.Retorno = Retorno

	def imprimir(self,espacio):
		print espacio+"Retorno del Metodo"
		self.Retorno.imprimir(espacio+' ')	

	def aceptar(self, visitante):
		return visitante.vTipoRetorno(self)
"""

class Argumetos(Nodo):
	def __init__(self, tipo, nombre, ListaArgumentos):
		self.nombre 		 = nombre
		self.tipo   		 = tipo
		self.ListaArgumentos = ListaArgumentos

	def imprimir(self,espacio):
		print espacio+"Argumeto "+self.nombre
		self.tipo.imprimir(espacio+' ')
		self.ListaArgumentos.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vArgumetos(self)

class ListaArgumentos(Nodo):
	def __init__(self, tipo,nombre,ListaArgumentos):
		self.nombre 		 = nombre
		self.tipo   		 = tipo
		self.ListaArgumentos = ListaArgumentos

	def imprimir(self,espacio):
		print espacio+"ListaArgumentos ".nombre
		self.tipo.imprimir(espacio+' ')
		self.ListaArgumentos.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vListaArgumentos(self)

class CuerpoMetodo(Nodo):
	def __init__(self, DeclaracionVariables, DeclaracionSentencias):
		self.nombre                = "Cuerpo del Metodo"
		self.DeclaracionVariables  = DeclaracionVariables
		self.DeclaracionSentencias = DeclaracionSentencias

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.DeclaracionVariables.imprimir(espacio+' ')
		self.DeclaracionSentencias.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vCuerpoMetodo(self)

class DeclaracionVariables(Nodo):
	def __init__(self, tipo, nombre, Inicializacion, ListaDeclaracionVariables):
		self.nombre                    = "Declaracion variable "+nombre
		self.tipo                      = tipo
		self.Inicializacion            = Inicializacion
		self.ListaDeclaracionVariables = ListaDeclaracionVariables

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.tipo.imprimir(espacio+' ')
		self.Inicializacion.imprimir(espacio+' ')
		self.ListaDeclaracionVariables.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vDeclaracionVariables(self)

class ListaDeclaracionVariables(Nodo):
	def __init__(self, tipo, nombre, Inicializacion, ListaDeclaracionVariables):
		self.nombre 				   = "Declaracion variable "+nombre
		self.tipo   				   = tipo
		self.Inicializacion            = Inicializacion
		self.ListaDeclaracionVariables = ListaDeclaracionVariables

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.tipo.imprimir(espacio+' ')
		self.Inicializacion.imprimir(espacio+' ')
		self.ListaDeclaracionVariables.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vListaDeclaracionVariables(self)

class DeclaracionSentenciasAsignacion(Nodo):
	def __init__(self, Asignacion):
		self.nombre 	= "Sentancia de Asignacion"
		self.Asignacion = Asignacion

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.Asignacion.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vDeclaracionSentenciasAsignacion(self)

class DeclaracionSentenciasInvocar(Nodo):
	def __init__(self, Invocar):
		self.nombre 	= "Sentancia de Invocar"
		self.Invocar = Invocar

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.Invocar.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vDeclaracionSentenciasInvocar(self)

class DeclaracionSentenciasRetorno(Nodo):
	def __init__(self, Expresion):
		self.nombre    = "Sentancia de Retorno"
		self.Expresion = Expresion

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.Expresion.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vDeclaracionSentenciasRetorno(self)

class DeclaracionSentenciasIf(Nodo):
	def __init__(self, Expresion, DeclaracionSentencias, SentenciaElse):
		self.nombre                = "Sentancia de If"
		self.Expresion             = Expresion
		self.DeclaracionSentencias = DeclaracionSentencias
		self.SentenciaElse         = SentenciaElse

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.Expresion.imprimir(espacio+' ')
		self.DeclaracionSentencias.imprimir(espacio+' ')
		self.SentenciaElse.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vDeclaracionSentenciasIf(self)

class DeclaracionSentenciasWhile(Nodo):
	def __init__(self, Expresion, DeclaracionSentencias):
		self.nombre                = "Sentancia de While"
		self.Expresion             = Expresion
		self.DeclaracionSentencias = DeclaracionSentencias

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.Expresion.imprimir(espacio+' ')
		self.DeclaracionSentencias.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vDeclaracionSentenciasWhile(self)

class DeclaracionSentenciasBreak(Nodo):
	def __init__(self):
		self.nombre = "Sentancia de Break"

	def imprimir(self,espacio):
		print espacio+self.nombre

	def aceptar(self, visitante):
		return visitante.vDeclaracionSentenciasBreak(self)

class DeclaracionSentenciasContinue(Nodo):
	def __init__(self):
		self.nombre = "Sentancia de Continue"

	def imprimir(self,espacio):
		print espacio+self.nombre

	def aceptar(self, visitante):
		return visitante.vDeclaracionSentenciasContinue(self)

class Asignacion(Nodo):
	def __init__(self,Ubicacion,Expresion):
		self.nombre    = "Asignacion"
		self.Ubicacion = Ubicacion
		self.Expresion = Expresion

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.Ubicacion.imprimir(espacio+' ')
		self.Expresion.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vAsignacion(self)

class UbicacionId(Nodo):
	def __init__(self,nombre):
		self.nombre = nombre

	def imprimir(self,espacio):
		print espacio+"Ubicacion "+self.nombre

	def aceptar(self, visitante):
		return visitante.vUbicacionId(self)

class UbicacionPuntero(Nodo):
	def __init__(self,Expresion,nombre):
		self.nombre    = nombre
		self.Expresion = Expresion

	def imprimir(self,espacio):
		print espacio+"Ubicacion puntero "+self.nombre
		self.Expresion.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vUbicacionPuntero(self)

class UbicacionExpresion(Nodo):
	def __init__(self,Expresion1,Expresion2):
		self.nombre    = "Ubicacion Expresiones"
		self.Expresion1 = Expresion1
		self.Expresion2 = Expresion2

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.Expresion1.imprimir(espacio+' ')
		self.Expresion2.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vUbicacionExpresion(self)

class Invocar(Nodo):
	def __init__(self,Metodo,Parametros):
		self.nombre     = "Invocar"
		self.Metodo     = Metodo
		self.Parametros = Parametros

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.Metodo.imprimir(espacio+' ')
		self.Parametros.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vInvocar(self)

class Metodo(Nodo):
	def __init__(self,nombre):
		self.nombre     = nombre

	def imprimir(self,espacio):
		print espacio+self.nombre

	def aceptar(self, visitante):
		return visitante.vMetodo(self)

class MetodoExpresiones(Nodo):
	def __init__(self,Expresion, nombre):
		self.nombre    = nombre
		self.Expresion = Expresion

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.Expresion.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vMetodoExpresiones(self)

class Parametros(Nodo):
	def __init__(self,Expresion, ListaParametros):
		self.nombre    		 = "Parametros"
		self.Expresion 		 = Expresion
		self.ListaParametros = ListaParametros

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.Expresion.imprimir(espacio+' ')
		self.ListaParametros.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vParametros(self)

class SentenciaElse(Nodo):
	def __init__(self,DeclaracionSentencias):
		self.nombre    		       = "Sentencia Else"
		self.DeclaracionSentencias = DeclaracionSentencias

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.DeclaracionSentencias.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vSentenciaElse(self)

class Expresion(Nodo):
	def __init__(self,TipoExpresion):
		self.nombre    	   = "Expresion"
		self.TipoExpresion = TipoExpresion

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.TipoExpresion.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vExpresion(self)

class ExpresionInstancia(Nodo):
	def __init__(self,nombre):
		self.nombre    	   = nombre

	def imprimir(self,espacio):
		print espacio+"Instancia a clases"+self.nombre

	def aceptar(self, visitante):
		return visitante.vExpresionInstancia(self)

class ExpresionArray(Nodo):
	def __init__(self,Tipo,Expresion):
		self.nombre    = "Inicia array"
		self.Tipo 	   = Tipo
		self.Expresion = Expresion

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.Tipo.imprimir(espacio+' ')
		self.Expresion.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vExpresionArray(self)

class ExpresionAccesoMetodo(Nodo):
	def __init__(self,Expresion):
		self.nombre    = "Acceso Metodo"
		self.Expresion = Expresion

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.Expresion.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vExpresionAccesoMetodo(self)

class ExpresionBinaria(Nodo):
	def __init__(self,Expresion1, OperadorBinario, Expresion2):
		self.nombre    		 = "Expresion Binaria"
		self.Expresion1 	 = Expresion1
		self.OperadorBinario = OperadorBinario
		self.Expresion2 	 = Expresion2

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.Expresion1.imprimir(espacio+' ')
		self.OperadorBinario.imprimir(espacio+' ')
		self.Expresion2.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vExpresionBinaria(self)

class ExpresionUnaria(Nodo):
	def __init__(self,OperadorUnario, Expresion):
		self.nombre    		 = "Expresion Unaria"
		self.OperadorUnario = OperadorUnario
		self.Expresion 	 = Expresion

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.OperadorUnario.imprimir(espacio+' ')
		self.Expresion.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vExpresionUnaria(self)

class ExpresionCompuesta(Nodo):
	def __init__(self,Expresion):
		self.nombre    		 = "Expresion Compuesta"
		self.Expresion 	 = Expresion

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.Expresion.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vExpresionCompuesta(self)

class OperadorBinario(Nodo):
	def __init__(self,Operador):
		self.nombre   = "Operador Binario"
		self.Operador = Operador

	def imprimir(self,espacio):
		print espacio+self.nombre
		print espacio+self.Operador

	def aceptar(self, visitante):
		return visitante.vOperadorBinario(self)

class OperadorUnario(Nodo):
	def __init__(self,Operador):
		self.nombre   = "Operador Unario"
		self.Operador = Operador

	def imprimir(self,espacio):
		print espacio+self.nombre
		print espacio+self.Operador

	def aceptar(self, visitante):
		return visitante.vOperadorUnario(self)

class Literales(Nodo):
	def __init__(self,Literal):
		self.nombre   = "Literal"
		self.Literal = Literal

	def imprimir(self,espacio):
		print espacio+self.nombre
		print espacio+self.Literal

	def aceptar(self, visitante):
		return visitante.vLiterales(self)

class Tipo(Nodo):
	def __init__(self,argumento):
		self.nombre   = "Tipo"
		self.argumento = argumento

	def imprimir(self,espacio):
		print espacio+self.nombre
		print espacio+self.argumento

	def aceptar(self, visitante):
		return visitante.vTipo(self)

class TipoCompuesto(Nodo):
	def __init__(self,Tipo):
		self.nombre   = "Tipo Compuesto"
		self.Tipo = Tipo

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.Tipo.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vTipoCompuesto(self)

class Inicializacion(Nodo):
	def __init__(self,Expresion):
		self.nombre   = "Inicializacion"
		self.Expresion = Expresion

	def imprimir(self,espacio):
		print espacio+self.nombre
		self.Expresion.imprimir(espacio+' ')

	def aceptar(self, visitante):
		return visitante.vInicializacion(self)

class DeclaracionesNull(Nodo):
	'''Se envian todas las produccines que producen landa'''
	def __init__(self):
		self.nombre = "Null"

	def imprimir(self,espacio):
		print espacio+self.nombre

	def aceptar(self, visitante):
		return visitante.vDeclaracionesNull(self)
