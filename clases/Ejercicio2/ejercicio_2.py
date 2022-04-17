class FilosofiaMVC:
    def __init__(self):
        self.mensaje=str(input("Introduzca el mensaje: "))
    
    def vista(self):
        troceado=self.troceador()
        f=open('clases.Ejercicio2.salida.txt', 'w','cp1252')
        print(f)
        f.write(troceado)
            

    
    def troceador(self):
        troceado=[]
        for i in self.mensaje:
            troceado.append(str(i.upper()))
        tyu="".join(troceado)
        return tyu

def main():
    h=FilosofiaMVC()
    h.vista()

if __name__=="__main__":
    main()
