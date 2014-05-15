import ply.yacc as yacc
import lexer as lex
from lexer import tokens
from classParser import *

precedence = (
	('right','ASIGNACION'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE'),
	('left', 'BOOLEAN_AND', 'BOOLEAN_OR'),
	#('left', 'LT', 'GT', 'EQ', 'NE', 'LE', 'GE'),
	('right', 'ELSE'),
	('right', 'BOOLEAN_NOT'),
    ('left','LPAREN','LBRACKET'),
)

def p_Programa(p):
	'Programa : ListaDeclaracion'
	p[0] = Programa(p[1])

def p_ListaDeclaracion(p):
	'ListaDeclaracion : DeclaracionClase ListaDeclaracion'
	p[0] = ListaDeclaracion(p[1], p[2])

def p_ListaDeclaracionNull(p):
	'ListaDeclaracion : empty'
	p[0] = ListaDeclaracionNull()

def p_DeclaracionClase(p):
	'DeclaracionClase : CLASS ID DeclaracionExtenciones LBRACE CuerpoClase RBRACE'
	p[0] = DeclaracionClase(Identificador(p[2],p.lineno(1)), p[3],p[5])

def p_DeclaracionExtenciones(p):
	'DeclaracionExtenciones : EXTENDS ID'
	p[0] = DeclaracionExtenciones(Identificador(p[2],p.lineno(1)))

def p_DeclaracionExtencionesNull(p):
	'DeclaracionExtenciones : empty'
	p[0] = DeclaracionExtencionesNull()

def p_CuerpoClaseAtributo(p):
	'CuerpoClase : DeclaracionAtributos'
	p[0] = CuerpoClaseAtributo(p[1])

def p_CuerpoClaseMetodo(p):
	'CuerpoClase : DeclaracionMetodos'
	p[0] = CuerpoClaseMetodo(p[1])


def p_CuerpoClaseNull(p):
	'CuerpoClase : empty'
	p[0] = CuerpoClaseNull()

def p_DeclaracionAtributos(p):
	'DeclaracionAtributos : DeclaracionAtributos Type ID SEMI'
	p[0] = DeclaracionAtributos(p[1], p[2], p[3])

def p_DeclaracionAtributo(p):
	'DeclaracionAtributos : Type ID COMMA'
	p[0] = DeclaracionAtributo(p[1], p[2])

def p_DeclaracionAtributoNull(p):
	'DeclaracionAtributos : empty'
	p[0] = DeclaracionAtributoNull()

def p_DeclaracionMetodos(p):
	'DeclaracionMetodos : Type ID LPAREN Argumentos RPAREN CuerpoMetodo'
	p[0] = DeclaracionMetodos(p[1], p[2], p[4], p[5])

def p_DeclaracionMetodosNull(p):
	'DeclaracionMetodos : empty'
	p[0] = DeclaracionMetodosNull()

def p_Argumentos(p):
	'Argumentos : Argumentos COMMA Type ID'
	p[0] = Argumentos(p[1], p[2], p[3])

def p_Argumento(p):
	'Argumentos : Type ID'
	p[0] = Argumento(p[1], p[2])

def p_ArgumentosNull(p):
	'Argumentos : empty'
	p[0] = ArgumentosNull()

def p_CuerpoMetodo(p):
	'CuerpoMetodo : LBRACE DeclaracionVariables DeclaracionSentencias RBRACE'
	p[0] = CuerpoMetodo(p[2], p[3])

def p_CuerpoMetodoNull(p):
	'CuerpoMetodo : empty'
	p[0] = CuerpoMetodoNull()

def p_DeclaracionVariablesNull(p):
	'DeclaracionVariables : empty'
	pass

def p_DeclaracionSentenciasNull(p):
	'DeclaracionSentencias : empty'
	pass

def p_Type(p):
	'''Type : INT
			| BOOLEAN
			| STRING
			| ID
	'''
	p[0] = Type(p[1])

def p_TypeNull(p):
	'Type : empty'
	p[0] = TypeNull()

def p_Empty(p):
	'empty :'
	pass

def p_error(p):
    print "Error de sintaxis ", p

yacc.yacc(method='LALR')

#raiz.imprimir()



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
    filename = input() 
    
    f = open("archivos_prueba/"+filename+".txt",r)
    data = f.read()
    f.close()
    
    raiz = yacc.parse(data)		
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