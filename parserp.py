import ply.yacc as yacc
import lexer as lex
from lexer import tokens
from classParser import *
from visitante import *

precedence = (    	
    ('left', 'IS_SMALLER', 'IS_SMALLER_OR_EQUAL', 'IS_GREATER', 'IS_GREATER_OR_EQUAL','BOOLEAN_OR','BOOLEAN_AND','IS_EQUAL', 'IS_NOT_EQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULE')    
)

def p_Programa(p):
	'Programa : ListaDeclaraciones'
	p[0] = Programa(p[1])

def p_PListaDeclaracionesNull(p):
	'ListaDeclaraciones : empty'
	p[0] = DeclaracionesNull()

def p_ListaDeclaraciones(p):
	'ListaDeclaraciones : DeclaracionClase ListaDeclaraciones'
	p[0] = ListaDeclaraciones(p[1],p[2])

def p_DeclaracionClase(p):
	'DeclaracionClase : CLASS ID DeclaracionExtenciones LBRACE CuerpoClase RBRACE'
	p[0] = DeclaracionClase(p[2], p[3], p[5])

def p_DeclaracionExtencionesNull(p):
	'DeclaracionExtenciones : empty'
	p[0] = DeclaracionesNull()

def p_DeclaracionExtenciones(p):
	'DeclaracionExtenciones : EXTENDS ID'
	p[0] = DeclaracionExtenciones(p[2])

"""def p_CuerpoClase(p):
	'''CuerpoClase : ListaAtribMetod'''
	p[0] = CuerpoClase(p[1])
"""

"""def p_ListaAtribMetod(p):
	'''ListaAtribMetod : DeclaracionAtributos
				   	   | DeclaracionMetodos
	'''
	p[0] = ListaAtribMetod(p[1])
"""

def p_CuerpoClase(p):
	'''CuerpoClase : ListaCuerpoClase CuerpoClase'''
	p[0] = CuerpoClase(p[1], p[2])

def p_CuerpoClaseAtributos(p):
	'''ListaCuerpoClase : DeclaracionAtributos'''
	p[0] = CuerpoClaseAtributos(p[1])

def p_CuerpoClaseMetodos(p):
	'''ListaCuerpoClase : DeclaracionMetodos'''
	p[0] = CuerpoClaseMetodos(p[1])

def p_CuerpoClaseNull(p):
	'''CuerpoClase : empty'''
	p[0] = DeclaracionesNull()


def p_DeclaracionAtributos(p):
	'DeclaracionAtributos : Tipo ID ListaAtributos SEMI DeclaracionAtributos'
	p[0] = DeclaracionAtributos(p[2], p[3],p[5])

def p_DeclaracionAtributosNull(p):
	'DeclaracionAtributos : empty'
	p[0] = DeclaracionesNull()

def p_ListaAtributos(p):
	'ListaAtributos : COMMA ID ListaAtributos'
	p[0] = ListaAtributos(p[2], p[3])

def p_ListaAtributosNull(p):
	'ListaAtributos : empty'
	p[0] = DeclaracionesNull()

def p_DeclaracionMetodos(p):
	'DeclaracionMetodos : Tipo ID LPAREN Argumetos RPAREN CuerpoMetodo'
	p[0] = DeclaracionMetodos(p[1], p[2], p[4], p[6])

def p_DeclaracionMetodosVoid(p):
	'DeclaracionMetodos : VOID ID LPAREN Argumetos RPAREN CuerpoMetodo'
	p[0] = DeclaracionMetodosVoid(p[1], p[2], p[4], p[6])

def p_Argumetos(p):
	'Argumetos : Tipo ID ListaArgumentos'
	p[0] = Argumetos(p[1],p[2],p[3])

def p_ArgumetosNull(p):
	'Argumetos : empty'
	p[0] = DeclaracionesNull()

def p_ListaArgumentos(p):
	'ListaArgumentos : COMMA Tipo ID ListaArgumentos'
	p[0] = ListaArgumentos(p[2],p[3],p[4])

def p_ListaArgumentosNull(p):
	'ListaArgumentos : empty'
	p[0] = DeclaracionesNull()

def p_CuerpoMetodo(p):
	'CuerpoMetodo : LBRACE DeclaracionVariables DeclaracionSentencias RBRACE'
	p[0] = CuerpoMetodo(p[2],p[3])

def p_DeclaracionVariables(p):
	'DeclaracionVariables : Tipo ID Inicializacion ListaDeclaracionVariables SEMI'
	p[0] = DeclaracionVariables(p[1],p[2],p[3],p[4])

def p_DeclaracionVariablesNull(p):
	'DeclaracionVariables : empty'
	p[0] = DeclaracionesNull()

def p_ListaDeclaracionVariables(p):
	'ListaDeclaracionVariables : COMMA Tipo ID Inicializacion ListaDeclaracionVariables'
	p[0] = ListaDeclaracionVariables(p[2], p[3], p[4], p[5])

def p_ListaDeclaracionVariablesNull(p):
	'ListaDeclaracionVariables : empty'
	p[0] = DeclaracionesNull()

def p_DeclaracionSentenciasAsignacion(p):
	'DeclaracionSentencias : Asignacion SEMI'
	p[0] = DeclaracionSentenciasAsignacion(p[1])

def p_DeclaracionSentenciasInvocar(p):
	'DeclaracionSentencias : Invocar SEMI'
	p[0] = DeclaracionSentenciasInvocar(p[1])

def p_DeclaracionSentenciasRetorno(p):
	'DeclaracionSentencias : RETURN Expresion SEMI'
	p[0] = DeclaracionSentenciasRetorno(p[2])

def p_DeclaracionSentenciasIf(p):
	'DeclaracionSentencias : IF LPAREN Expresion RPAREN LBRACE DeclaracionSentencias RBRACE SentenciaElse'
	p[0] = DeclaracionSentenciasIf(p[3],p[6],p[8])

def p_DeclaracionSentenciasWhile(p):
	'DeclaracionSentencias : WHILE LPAREN Expresion RPAREN LBRACE DeclaracionSentencias RBRACE'
	p[0] = DeclaracionSentenciasWhile(p[3],p[6])

def p_DeclaracionSentenciasBreak(p):
	'DeclaracionSentencias : BREAK SEMI'
	p[0] = DeclaracionSentenciasBreak()

def p_DeclaracionSentenciasContinue(p):
	'DeclaracionSentencias : CONTINUE SEMI'
	p[0] = DeclaracionSentenciasContinue()

def p_DeclaracionSentenciasNull(p):
	'DeclaracionSentencias : empty'
	p[0] = DeclaracionesNull()

def p_Asignacion(p):
	'Asignacion : Ubicacion ASIGNACION Expresion'
	p[0] = Asignacion(p[1],p[2])

def p_UbicacionId(p):
	'Ubicacion : ID'
	p[0] = UbicacionId(p[1])

def p_Ubicacion(p):
	'Ubicacion : Expresion METHOD_ACCESS ID'
	p[0] = UbicacionPuntero(p[1],p[3])

def p_UbicacionExpresion(p):
	'Ubicacion : Expresion LBRACKET Expresion RBRACKET'
	p[0] = UbicacionExpresion(p[1],p[3])

def p_Invocar(p):
	'Invocar : Metodo LPAREN Parametros RPAREN'
	p[0] = Invocar(p[1],p[3])

def p_Metodo(p):
	'Metodo : ID'
	p[0] = Metodo(p[1])

def p_MetodoExpresiones(p):
	'Metodo : Expresion METHOD_ACCESS ID'
	p[0] = MetodoExpresiones(p[1],p[3])

def p_Parametros(p):
	'Parametros : Expresion ListaParametros'
	p[0] = Parametros(p[1],p[2])

def p_ParametrosNull(p):
	'Parametros : empty'
	p[0] = DeclaracionesNull()

def p_ListaParametros(p):
	'ListaParametros : COMMA Expresion ListaParametros'
	p[0] = Parametros(p[2], p[3])

def p_ListaParametrosNull(p):
	'ListaParametros : empty'
	p[0] = DeclaracionesNull()

def p_SentenciaElse(p):
	'SentenciaElse : ELSE DeclaracionSentencias'
	p[0] = SentenciaElse(p[2])

def p_SentenciaElseNull(p):
	'SentenciaElse : empty'
	p[0] = DeclaracionesNull()

def p_Expresion(p):
	'''Expresion : Ubicacion
				 | Invocar
				 | THIS
				 | Literales
	'''
	p[0] = Expresion(p[1])

def p_ExpresionArray(p):
	'Expresion : NEW Tipo LBRACKET Expresion RBRACKET'
	p[0] = ExpresionArray(p[2],p[4])

def p_ExpresionInstancia(p):
	'Expresion : NEW ID LPAREN  RPAREN'
	p[0] = ExpresionInstancia(p[2])


def p_ExpresionAccesoMetodo(p):
	'Expresion : Expresion METHOD_ACCESS LENGTH'
	p[0] = ExpresionAccesoMetodo(p[1])

def p_ExpresionBinaria(p):
	'''Expresion : Expresion PLUS Expresion
				 | Expresion MINUS Expresion	
				 | Expresion TIMES Expresion
				 | Expresion DIVIDE Expresion
				 | Expresion MODULE Expresion
				 | Expresion BOOLEAN_AND Expresion
				 | Expresion BOOLEAN_OR Expresion	
				 | Expresion IS_SMALLER_OR_EQUAL Expresion
				 | Expresion IS_GREATER_OR_EQUAL Expresion
				 | Expresion IS_SMALLER Expresion
				 | Expresion IS_GREATER Expresion
				 | Expresion IS_EQUAL Expresion
				 | Expresion IS_NOT_EQUAL Expresion
	'''
	p[0] = ExpresionBinaria(p[1], p[2], p[3])

def p_ExpresionUnaria(p):
	'Expresion : OperadorUnario Expresion'
	p[0] =ExpresionUnaria(p[1], p[2])

def p_ExpresionCompuesta(p):
	'Expresion : LPAREN Expresion RPAREN'
	p[0] = ExpresionCompuesta(p[2])

def p_OperadorUnario(p):
	'''OperadorUnario : MINUS
					  | BOOLEAN_NOT
	'''
	p[0] = OperadorUnario(p[1])

def p_Literales(p):
	'''Literales : NUMBEREX
				 | NUMBER
				 | CSTRING
				 | TRUE
				 | FALSE
				 | NULL

	'''
	p[0] = Literales(p[1])

def p_Tipo(p):
	'''Tipo : INT
			| BOOLEAN
			| STRING
	'''
	p[0] = Tipo(p[1])

def p_TipoCompuesto(p):
	'Tipo : Tipo LBRACKET RBRACKET'
	p[0] = TipoCompuesto(p[1])

def p_Inicializacion(p):
	'Inicializacion : ASIGNACION Expresion'
	p[0] = Inicializacion(p[2])

def p_InicializacionNull(p):
	'Inicializacion : empty'
	p[0] = DeclaracionesNull()

def p_Empty(p):
	'empty :'
	pass

def p_error(p):
    print "Error de sintaxis ", p


'''
Funcion para leer el codigo funente desde un archivo
y pasar al parser las cadenas de caracteres a analizar

@function leer_archivo
@param  void
@return void
'''
def leer_archivo_yacc():
    '''
    Abre el archivo y lee linea a linea poniendo las
    cadenas de caracteres de cada linea en la intrada
    del analizador lexico
    '''

    yacc.yacc(method='LALR')

    s = raw_input(">> ")

    with open('archivos_prueba_parser/'+s+'.txt') as linea:
        datos = linea.read()
        raiz = yacc.parse(datos)        
        v = Visitante()
	print raiz.aceptar(v)
	print v


    '''
    Loop infinido que muestra los token's reconocidos por
    el analizador sintactico dando informacion de:
    tipo de token
    valor del token
    fila donde fue leido
    columna donde fue leido
    cuando no encuentra mas token's en la entrada termina
    la iteracion
    '''
    '''while True:
        tok = lexer.token()
        if not tok: break # Si no encuentra token's detiene las iteraciones
        #print "Tipo: %s Valor '%s' Fila %d Columna %d" %(tok.type, tok.value, tok.lineno, obtener_columna(tok.lexer.lexdata, tok))
    print raiz'''

leer_archivo_yacc()