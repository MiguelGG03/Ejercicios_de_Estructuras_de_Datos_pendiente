from clases.Ejercicio1.ejercicio_1 import *
from clases.Ejercicio2.ejercicio_2 import *
from clases.Ejercicio3.ejercicio_3 import *




def main():
    acabar=False
    while(acabar==False):
        seguir=str(input('Quieres seguir viendo ejercicios(S/N)?:'))    
        if(seguir=='s' or seguir=='S'):
            cual=str(input('Que ejercicio quieres ver (1,2,3)?:'))
            if(cual=='1'):
                print('EJERCICIO 1:\n')
                nivel=0
                mostrar_ok = Mostrar('"OK"') 
                mostrar_ko = Mostrar('"KO"') 
                alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko) 
                bloque_alternativa = Bloque() 
                bloque_alternativa.agregarInstruccion(alternativa)
                bucle = MientrasQue(True, bloque_alternativa) 
                bucle.pintarMientras(nivel)

            elif(cual=='2'):
                print('EJERCICIO 2:\n')
                h=FilosofiaMVC()
                h.vista()

            elif(cual=='3'):
                print('EJERCICIO 3:\n')
                ejercicio6()
            else:
                print('Eso no es un 1, un 2 o un 3.')
        if(seguir=='n' or seguir=='N'):
            acabar=True
        else:
            print('Introduzca una N o una S')


if __name__=='__main__':
    main()