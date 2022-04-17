class FilosofiaMVC:

    def __init__(self):
        self.mensaje1=str(input("Introduzca el mensaje: "))
        self.mensaje2=str(input("Introduzca el mensaje: "))
    
    

    def vista(self):
        troceado=self.troceador()
        f=open('salida.txt', 'w')
        f.write(troceado)
        f.close
        self.f=f



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

def main():
    h=FilosofiaMVC()
    h.vista()

if __name__=="__main__":
    main()
