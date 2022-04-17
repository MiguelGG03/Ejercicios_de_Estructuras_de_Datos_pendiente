class Bloque:
    def __init__(self): 
        self.instrucciones = []
 
    def agregarInstruccion(self, instruccion): 
        self.instrucciones.append(instruccion)
    
    def 

    def pintarInstruccion(self):
        for i in range(0,len(self.instrucciones)):
            if(isinstance(self.instrucciones[i],Si)):
                self.instrucciones[i].pintarIf()
            if(isinstance(self.instrucciones[i],Mostrar)):
                self.instrucciones[i].pintarMostrar()
            if(isinstance(self.instrucciones[i],MientrasQue)):
                self.instrucciones[i].pintarMientras()


class Si: 
    def __init__(self, condicion, entonces, sino): 
        self.condicion = condicion 
        self.entonces = entonces 
        self.sino = sino
    
    def pintarIf(self):
        print( "if ("+self.condicion+"):")
        if(isinstance(self.entonces,Mostrar)):
            self.entonces.pintarMostrar()
        else:
            print("{}".format(self.entonces))
        print( "else:")
        if(isinstance(self.sino,Mostrar)):
            self.sino.pintarMostrar()
        else:
            print("{}".format(self.sino))


class MientrasQue:  
    def __init__(self, condicion, bloque): 
        self.condicion = condicion 
        self.bloque = bloque

    def pintarMientras(self):
        print("while({}):".format(self.condicion))
        self.bloque.pintarInstruccion()


 
class Mostrar: 
    def __init__(self, mensaje): 
        self.mensaje = mensaje

    def pintarMostrar(self):
        print("print({})".format(self.mensaje))




def main():
    nicel=0
    mostrar_ok = Mostrar('"OK"') 
    mostrar_ko = Mostrar('"KO"') 
    alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko) 
    bloque_alternativa = Bloque() 
    bloque_alternativa.agregarInstruccion(alternativa) 
    bucle = MientrasQue(True, bloque_alternativa) 
    bucle.pintarMientras()



if __name__=="__main__":
    main()




    #itertools.repeat(val,num)