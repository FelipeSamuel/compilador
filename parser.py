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

def p_CuerpoClase(p):
	'CuerpoClase : empty'
	p[0] = CuerpoClaseNull()
	pass

def p_Empty(p):
	'empty :'
	pass

def p_error(p):
    print "Error de sintaxis ", p

yacc.yacc(method='LALR')

raiz = yacc.parse("class juan {}")
print raiz

raiz.imprimir()
