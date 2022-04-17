class Bloque:
    def __init__(self): 
        self.instrucciones = []
 
    def agregarInstruccion(self, instruccion): 
        self.instrucciones.append(instruccion)

    def leerInstruccion(self,que_instruccion):
        return self.instrucciones[que_instruccion]


class Si: 
    def __init__(self, condicion, entonces, sino): 
        self.condicion = condicion 
        self.entonces = entonces 
        self.sino = sino


class MientrasQue:  
    def __init__(self, condicion, bloque): 
        self.condicion = condicion 
        self.bloque = bloque

 
class Mostrar: 
    def __init__(self, mensaje): 
        self.mensaje = mensaje





def main():
    mostrar_ok = Mostrar('"OK"') 
    mostrar_ko = Mostrar('"KO"') 
    alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko) 
    bloque_alternativa = Bloque() 
    bloque_alternativa.agregarInstruccion(alternativa) 
    bucle = MientrasQue(True, bloque_alternativa) 
    print(bloque_alternativa.leerInstruccion(0))


if __name__=="__main__":
    main()