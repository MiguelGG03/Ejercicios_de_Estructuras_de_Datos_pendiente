# Ejercicios_de_Estructuras_de_Datos_pendiente

El enlace al repositorio es el siguiente: [GitHub](https://github.com/migueliiin/Ejercicios_de_Estructuras_de_Datos_pendiente.git)

### Ejercicio 1

Código del ejercicio 1:

 ```
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
 ```
 
 ### Ejercicio 2

Código del ejercicio 2:

 ```
 class FilosofiaMVC:

    def __init__(self):
        self.mensaje1=str(input("Introduzca el mensaje: "))
        self.mensaje2=str(input("Introduzca el mensaje: "))
    
    

    def vista(self):
        troceado=self.troceador()
        f=open('salida.txt', 'w')
        f.write(troceado)
        f.close



    def troceador(self):
        t1=[]
        t2=[]
        troceado=[]
        for i in self.mensaje1:
            t1.append(str(i.upper()))
        for i in self.mensaje2:
            t2.append(str(i.upper()))
        tyu1="".join(t1)
        tyu2="".join(t2)
        troceado.append(tyu1)
        troceado.append(tyu2)
        tyu="\n".join(troceado)
        print(tyu)
        return tyu
 ```
