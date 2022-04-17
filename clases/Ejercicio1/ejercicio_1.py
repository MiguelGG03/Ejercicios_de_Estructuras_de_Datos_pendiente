class Bloque:
    def __init__(self): 
        self.instrucciones = []
 
    def agregarInstruccion(self, instruccion): 
        self.instrucciones.append(instruccion)

    def pintarInstruccion(self,nivel):
        for i in range(0,len(self.instrucciones)):
            if(isinstance(self.instrucciones[i],Si)):
                nivel=self.instrucciones[i].pintarIf(nivel)
            if(isinstance(self.instrucciones[i],Mostrar)):
                nivel=self.instrucciones[i].pintarMostrar(nivel)
            if(isinstance(self.instrucciones[i],MientrasQue)):
                nivel=self.instrucciones[i].pintarMientras(nivel)
        return nivel

class Si: 
    def __init__(self, condicion, entonces, sino): 
        self.condicion = condicion 
        self.entonces = entonces 
        self.sino = sino
    
    def pintarIf(self,nivel):
        tab="    "*nivel
        tab2="    "*(nivel+1)
        print( "{}if ({}):".format(tab,self.condicion))
        if(isinstance(self.entonces,Mostrar)):
            self.entonces.pintarMostrar(nivel+1)
        else:
            print("{}{}".format(tab2,self.entonces))
        print( "{}else:".format(tab))
        if(isinstance(self.sino,Mostrar)):
            self.sino.pintarMostrar(nivel+1)
        else:
            print("{}{}".format(tab2,self.sino))
        return nivel


class MientrasQue:  
    def __init__(self, condicion, bloque): 
        self.condicion = condicion 
        self.bloque = bloque

    def pintarMientras(self,nivel):
        tab="    "*nivel
        print("{}while({}):".format(tab,self.condicion))
        nivel=self.bloque.pintarInstruccion(nivel+1)
        return (nivel-1)


 
class Mostrar: 
    def __init__(self, mensaje): 
        self.mensaje = mensaje

    def pintarMostrar(self,nivel):
        tab="    "*nivel
        print("{}print({})".format(tab,self.mensaje))
        return nivel


