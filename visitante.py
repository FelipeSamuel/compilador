class Nodo:
    pass

class Visitante(Nodo):

    def __init__(self):
        self.txt = "digraph G {\n\t"
        self.id = 0

    def __str__(self):
        return self.txt + "\t}"

    def incrementarId(self):
        self.id += 1
        return "%d " % self.id

    def vPrograma(self, nodo):
        id = self.incrementarId()
        ListaDeclaraciones = nodo.ListaDeclaraciones.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + ListaDeclaraciones + "\n\t"
        return id

    def vListaDeclaraciones(self, nodo):
        id = self.incrementarId()
        DeclaracionClase   = nodo.DeclaracionClase.aceptar(self)
        ListaDeclaraciones = nodo.ListaDeclaraciones.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + DeclaracionClase + "\n\t"
        self.txt += id + " -> " + ListaDeclaraciones + "\n\t"
        return id

    def vDeclaracionClase(self, nodo):
        id = self.incrementarId()
        DeclaracionExtenciones = nodo.DeclaracionExtenciones.aceptar(self)
        CuerpoClase = nodo.CuerpoClase.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + DeclaracionExtenciones + "\n\t"
        self.txt += id + " -> " + CuerpoClase + "\n\t"

        return id

    def  vDeclaracionExtenciones(self, nodo):
        id = self.incrementarId()

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"

        return id

    def vCuerpoClase(self, nodo):
        id = self.incrementarId()
        ListaCuerpoClase = nodo.ListaCuerpoClase.aceptar(self)
        CuerpoClase = nodo.CuerpoClase.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + ListaCuerpoClase + "\n\t"
        self.txt += id + " -> " + CuerpoClase + "\n\t"

        return id

    def vCuerpoClaseAtributos(self, nodo):
        id = self.incrementarId()
        DeclaracionAtributos = nodo.DeclaracionAtributos.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + DeclaracionAtributos + "\n\t"

        return id

    def vCuerpoClaseMetodos(self, nodo):
        id = self.incrementarId()

        DeclaracionMetodos = nodo.DeclaracionMetodos.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + DeclaracionMetodos + "\n\t"

        return id

    def vListaAtribMetod(self, nodo):
        id = self.incrementarId()

        Declaraciones = nodo.Declaraciones.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + Declaraciones + "\n\t"

        return id

    def vDeclaracionAtributos(self, nodo):
        id = self.incrementarId()

        ListaAtributos = nodo.ListaAtributos.aceptar(self)
        DeclaracionAtributos = nodo.DeclaracionAtributos.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + ListaAtributos + "\n\t"
        self.txt += id + " -> " + DeclaracionAtributos + "\n\t"

        return id

    def vListaAtributos(self, nodo):
        id = self.incrementarId()

        ListaAtributos = nodo.ListaAtributos.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + ListaAtributos + "\n\t"

        return id

    def vDeclaracionMetodos(self, nodo):
        id = self.incrementarId()

        Argumetos   = nodo.Argumetos.aceptar(self)
        CuerpoMetodo = nodo.CuerpoMetodo.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        #self.txt += id + " -> [label= "+ nodo.TipoRetorno +"]\n\t"        
        self.txt += id + " -> " + Argumetos + "\n\t"
        self.txt += id + " -> " + CuerpoMetodo + "\n\t"

        return id

    def vDeclaracionMetodosVoid(self, nodo):
        id = self.incrementarId()
        
        Argumetos   = nodo.Argumetos.aceptar(self)
        CuerpoMetodo = nodo.CuerpoMetodo.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> [label= "+ nodo.TipoRetorno +"]\n\t"        
        self.txt += id + " -> " + Argumetos + "\n\t"
        self.txt += id + " -> " + CuerpoMetodo + "\n\t"

        return id

    def vTipoRetorno(self, nodo):
        id = self.incrementarId()

        Retorno = nodo.Retorno.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + Retorno + "\n\t"

        return id

    def vArgumetos(self, nodo):
        id = self.incrementarId()

        tipo = nodo.tipo.aceptar(self)
        ListaArgumentos = nodo.ListaArgumentos.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + tipo + "\n\t"
        self.txt += id + " -> " + ListaArgumentos + "\n\t"

        return id

    def vListaArgumentos(self, nodo):
        id = self.incrementarId()

        tipo = nodo.tipo.aceptar(self)
        ListaArgumentos = nodo.ListaArgumentos.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + tipo + "\n\t"
        self.txt += id + " -> " + ListaArgumentos + "\n\t"

        return id

    def vCuerpoMetodo(self, nodo):
        id = self.incrementarId()

        DeclaracionVariables = nodo.DeclaracionVariables.aceptar(self)
        DeclaracionSentencias = nodo.DeclaracionSentencias.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + DeclaracionVariables + "\n\t"
        self.txt += id + " -> " + DeclaracionSentencias + "\n\t"

        return id

    def vDeclaracionVariables(self, nodo):
        id = self.incrementarId()

        tipo = nodo.tipo.aceptar(self)
        Inicializacion = nodo.Inicializacion.aceptar(self)
        ListaDeclaracionVariables = nodo.ListaDeclaracionVariables.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + tipo + "\n\t"
        self.txt += id + " -> " + Inicializacion + "\n\t"
        self.txt += id + " -> " + ListaDeclaracionVariables + "\n\t"

        return id

    def vListaDeclaracionVariables(self, nodo):
        id = self.incrementarId()

        tipo = nodo.tipo.aceptar(self)
        Inicializacion = nodo.Inicializacion.aceptar(self)
        ListaDeclaracionVariables = nodo.ListaDeclaracionVariables.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + tipo + "\n\t"
        self.txt += id + " -> " + Inicializacion + "\n\t"
        self.txt += id + " -> " + ListaDeclaracionVariables + "\n\t"

        return id

    def vDeclaracionSentenciasAsignacion(self, nodo):
        id = self.incrementarId()

        Invocar = nodo.Invocar.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + Invocar + "\n\t"

        return id

    def vDeclaracionSentenciasInvocar(self, nodo):
        id = self.incrementarId()

        Invocar = nodo.Invocar.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + Invocar + "\n\t"

        return id

    def vDeclaracionSentenciasRetorno(self, nodo):
        id = self.incrementarId()

        Expresion = nodo.Expresion.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + ".... -> " + Expresion + "\n\t"

        return id

    def vDeclaracionSentenciasIf(self, nodo):
        id = self.incrementarId()

        Expresion = nodo.Expresion.aceptar(self)
        DeclaracionSentencias = nodo.DeclaracionSentencias.aceptar(self)
        SentenciaElse = nodo.SentenciaElse.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + Expresion + "\n\t"
        self.txt += id + " -> " + DeclaracionSentencias + "\n\t"
        self.txt += id + " -> " + SentenciaElse + "\n\t"

        return id

    def vDeclaracionSentenciasWhile(self, nodo):
        id = self.incrementarId()

        Expresion = nodo.Expresion.aceptar(self)
        DeclaracionSentencias = nodo.DeclaracionSentencias.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + Expresion + "\n\t"
        self.txt += id + " -> " + DeclaracionSentencias + "\n\t"

        return id

    def vDeclaracionSentenciasBreak(self, nodo):
        id = self.incrementarId()

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"

        return id

    def vDeclaracionSentenciasContinue(self, nodo):
        id = self.incrementarId()

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"

        return id

    def vAsignacion(self, nodo):
        id = self.incrementarId()

        Ubicacion = nodo.Ubicacion.aceptar(self)
        Expresion = nodo.Expresion.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + Ubicacion + "\n\t"
        self.txt += id + " -> " + Expresion + "\n\t"

        return id

    def vUbicacionId(self, nodo):
        id = self.incrementarId()

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"

        return id

    def vUbicacionPuntero(self, nodo):
        id = self.incrementarId()

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"

        return id

    def vUbicacionExpresion(self, nodo):
        id = self.incrementarId()

        Expresion1 = nodo.Expresion1.aceptar(self)
        Expresion2 = nodo.Expresion2.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + Expresion1 + "\n\t"
        self.txt += id + " -> " + Expresion2 + "\n\t"

        return id

    def vInvocar(self, nodo):
        id = self.incrementarId()

        Metodo = nodo.Metodo.aceptar(self)
        Parametros = nodo.Parametros.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + Metodo + "\n\t"
        self.txt += id + " -> " + Parametros + "\n\t"

        return id

    def vMetodo(self, nodo):
        id = self.incrementarId()

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"

        return id

    def vMetodoExpresiones(self, nodo):
        id = self.incrementarId()

        Expresion= nodo.Expresion.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + Expresion + "\n\t"

        return id

    def vParametros(self, nodo):
        id = self.incrementarId()

        Expresion= nodo.Expresion.aceptar(self)
        ListaParametros = nodo.ListaParametros.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + Expresion + "\n\t"
        self.txt += id + " -> " + ListaParametros + "\n\t"

        return id

    def vSentenciaElse(self, nodo):
        id = self.incrementarId()

        DeclaracionSentencias= nodo.DeclaracionSentencias.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + DeclaracionSentencias + "\n\t"

        return id

    def vExpresion(self, nodo):
        id = self.incrementarId()

        TipoExpresion= nodo.TipoExpresion.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + TipoExpresion + "\n\t"

        return id

    def vExpresionInstancia(self, nodo):
        id = self.incrementarId()

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"

        return id

    def vExpresionArray(self, nodo):
        id = self.incrementarId()

        Tipo= nodo.Tipo.aceptar(self)
        Expresion= nodo.Expresion.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + Tipo + "\n\t"
        self.txt += id + " -> " + Expresion + "\n\t"

        return id

    def vExpresionAccesoMetodo(self, nodo):
        id = self.incrementarId()

        Expresion= nodo.Expresion.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + Expresion + "\n\t"

        return id

    def vExpresionBinaria(self, nodo):
        id = self.incrementarId()

        Expresion1= nodo.Expresion1.aceptar(self)
        OperadorBinario = nodo.OperadorBinario.aceptar(self)
        Expresion2= nodo.Expresion2.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + Expresion1 + "\n\t"
        self.txt += id + " -> " + OperadorBinario + "\n\t"
        self.txt += id + " -> " + Expresion2 + "\n\t"

        return id

    def vExpresionUnaria(self, nodo):
        id = self.incrementarId()

        Expresion= nodo.Expresion.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + Expresion + "\n\t"

        return id

    def vExpresionCompuesta(self, nodo):
        id = self.incrementarId()

        OperadorUnario = nodo.OperadorUnario.aceptar(self)
        Expresion= nodo.Expresion.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> " + OperadorUnario + "\n\t"
        self.txt += id + " -> " + Expresion + "\n\t"

        return id

    def vOperadorBinario(self, nodo):
        id = self.incrementarId()

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> [label= "+ nodo.Operador +"]\n\t"

        return id

    def vOperadorUnario(self, nodo):
        id = self.incrementarId()

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> [label= "+ nodo.Operador +"]\n\t"

        return id

    def vLiterales(self, nodo):
        id = self.incrementarId()

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> [label= "+ nodo.Literal +"]\n\t"

        return id

    def vTipo(self, nodo):
        id = self.incrementarId()

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> [label= "+ nodo.argumento +"]\n\t"

        return id

    def vTipoCompuesto(self, nodo):
        id = self.incrementarId()

        Tipo = nodo.Tipo.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> "+ Tipo +"\n\t"

        return id

    def vInicializacion(self, nodo):
        id = self.incrementarId()

        Expresion = nodo.Expresion.aceptar(self)

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"
        self.txt += id + " -> "+ Expresion +"\n\t"

        return id

    def vDeclaracionesNull(self, nodo):
        id = self.incrementarId()

        self.txt += id + " [label= "+nodo.nombre+"]\n\t"

        return id