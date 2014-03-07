# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

'''
Diccionario de datos que contiene la lista de las
palabras reservadas

@var reserved diccionario
'''
reserved = {
  'class'    : 'CLASS',
  'extends'  : 'EXTENDS',
  'void'     : 'VOID',
  'int'      : 'INT',
  'boolean'  : 'BOOLEAN',
  'string'   : 'STRING',
  'return'   : 'RETURN',
  'if'       : 'IF',
  'else'     : 'ELSE',
  'while'    : 'WHILE',
  'break'    : 'BREAK',
  'continue' : 'CONTINUE',
  'this'     : 'THIS',
  'new'      : 'NEW',
  'length'   : 'LENGTH',
  'true'     : 'TRUE',
  'false'    : 'FALSE',
  'null'     : 'NULL'
}

'''
Lista que contiene los token's del lenguaje
a esta lista se le agrega el diccionario de
datos que contiene las palabras reservadas

@var token lista
'''
tokens = [
            'ID',
            'NID',
            'BCOMMENT',
            'LCOMMENT',
            'ECOMMENT',
            'NUMBER'
         ] + list(reserved.values())


'''
Lexema para reconocer numeros.
@function t_NUMBER
@param  t (instancia del simbolo)
@return t (instancia del simbolo)
'''
def t_NUMBER(t):
    r'[+-]?(\d*\.\d+|\d+\.\d*)([Ee][+-]?\d+)? | (\d+[Ee][+-]?\d+)'    
    #r'[+-]?((0|[1-9][0-9]*)\.\d+)'    
    return t

'''
Lexema para reconocer identificadores no validos.
Hace las siguientes validaciones:
  * Si existe una cadena de entrada que empieza con
    numeros saca el error de identificador invalido    
@function t_NID
@param  t (instancia del simbolo)
@return t (instancia del simbolo)
'''
def t_NID(t):
    r'[0-9][a-zA-Z_0-9\-\_]*'
    print "ERROR: Identificador '%s' invalido en la linea %d columna %d" % (t.value, t.lexer.lineno, obtener_columna(t.lexer.lexdata, t))        

'''
Lexema para reconocer identificadores.
Hace las siguientes validaciones:
  * Que le identificador no se encuentre
    entre las palabras reservadas
  * Si la longitud del identificador tiene
    mas de 20 caracteres devuelve los primeros
    20 caracteres
@function t_ID
@param  t (instancia del simbolo)
@return t (instancia del simbolo)
'''
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9\-\_]*'
    t.type = reserved.get(t.value,'ID')
    if len(t.value) > 20:
      t.value = t.value[0:20]    
    return t

'''
Lexema para reconocer lineas comentadas
@function t_LCOMMENT
@param  t (instancia del simbolo)
@return t (instancia del simbolo)
'''
def t_LCOMMENT(t):
    r'//(.)*'    
    return t

'''
Lexema para reconocer bloques de lineas comentadas
@function t_BCOMMENT
@param  t (instancia del simbolo)
@return t (instancia del simbolo)
'''
def t_BCOMMENT(t):
    r'/\*(.|\n|\r|\t)*?\*/'
    t.lexer.lineno += t.value.count("\n")
    return t

'''
Lexema para reconocer error del no cierre del bloque 
comentarios
@function t_ECOMMENT
@param  t (instancia del simbolo)
@return t (instancia del simbolo)
'''
def t_ECOMMENT(t):
    r'/\*(.|\n|\r|\t)*?'    
    print "FATAL ERROR: El bloque de comentario '%s' no esta cerrado linea %d columna %d" % (t.value, t.lexer.lineno, obtener_columna(t.lexer.lexdata, t))        
    exit(0)

'''
list(reserved.values())
# List of token names.   This is always required
tokens = (   
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
'''

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

'''
Funcion para la gestion de errores

Los token's no encontrados los muestra como caracteres invalidos
lueog omite el error y continua con la ejecucion del programa
@function t_error
@param  t     (instancia del simbolo)
@return void
'''
def t_error(t):
    print "ERROR: Token '%s' no reconocido en la linea %d columna %d" % (t.value[0], t.lexer.lineno, obtener_columna(t.lexer.lexdata, t))
    t.lexer.skip(1)

'''
Funcion para leer el codigo funente desde un archivo
y pasar al lexer las cadenas de caracteres a analizar

@function leer_archivo
@param  void
@return void
'''
def leer_archivo():
    '''
    Abre el archivo y lee linea a linea poniendo las
    cadenas de caracteres de cada linea en la intrada
    del analizador lexico
    '''
    with open('archivos_prueba/numeros.txt') as linea:
        datos = linea.read()
        lexer.input(datos)
    '''
    Loop infinido que muestra los token's reconocidos por
    el analizador lexico dando informacion de:
    tipo de token
    valor del token
    fila donde fue leido
    columna donde fue leido
    cuando no encuentra mas token's en la entrada termina
    la iteracion
    '''
    while True:
        tok = lexer.token()
        if not tok: break # Si no encuentra token's detiene las iteraciones
        print "Tipo: %s Valor '%s' Fila %d Columna %d" %(tok.type, tok.value, tok.lineno, obtener_columna(tok.lexer.lexdata, tok))

'''
Funcion para determinar la columna donde se encuentra
ubicado el token leido

@function obtener_columna
@param  cadena  (cadena de entrada)
@param  token   (instancia del simbolo)
@return columna (posicion de la columna donde empieza el token)
'''
def obtener_columna(cadena,token):
  ultimo_salto = cadena.rfind('\n',0,token.lexpos) #determina la posicion inmediatamente anterior del ultimo salto de linea que encuentre en la cadena
  '''
  token.lexpos posicion del primer caracter del token encontrado
  haciendo la resta en el token.lexpos - ultimo_salto se obtiene
  la posicion de la  columna en donde empieza el token
  '''
  columna = (token.lexpos - ultimo_salto)
  return columna


'''
Constructor del analizador lexico
'''
lexer = lex.lex()

'''
Llamada inicial para comenzar a leer los token's
del archivo
'''
leer_archivo()