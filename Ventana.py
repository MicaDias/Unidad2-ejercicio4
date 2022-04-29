class Ventana:
    __titulo=''
    __xSupizquierdo=0
    __ySupizquierdo=0
    __xInfderecho=0
    __yInfderecho=0
    def __init__(self,titulo='',xSupizquierdo=0,ySupizquierdo=0,xInfderecho=500,yInfderecho=500):
        self.__titulo=titulo
        self.__xSupizquierdo=xSupizquierdo
        self.__ySupizquierdo=ySupizquierdo
        self.__xInfderecho=xInfderecho
        self.__yInfderecho=yInfderecho
    def mostrar(self):
        print("Titulo:{},coordenadas del vertice superior izquierdo x:{}, y:{}, coordenadas del vertice inferior derecho x:{},y:{}".format(self.__titulo, self.__xSupizquierdo, self.__ySupizquierdo,self.__xInfderecho,self.__yInfderecho))
    def getTitulo(self):
        return self.__titulo
    def alto(self):
        alt=self.__yInfderecho-self.__ySupizquierdo
        return alt
    def ancho(self):
        anc=self.__xInfderecho-self.__xSupizquierdo
        return anc
    def moverDerecha(self,desp=0):
        suma=self.__xInfderecho+desp
        if(suma<=500):
            suma1=xSupizquierdo+desp
            self.__xSupizquierdo=suma1
            self.__xInfderecho=suma
        else:
            print("no se pudo realizar la operacion")
    def moverIzquierda(self,desp=0): 
        resta=self.__xSupizquierdo-desp
        if(resta>=0):
            resta1=self.__xInfderecho-desp
            self.__xSupizquierdo=resta
            self.__xInfderecho=resta1
        else:
            print("no se pudo realizar la operacion")
    def subir(self,despA=0):
        restar=self.__ySupizquierdo-despA
        if(restar>=0):
            restar1=self.__yInfderecho-despA
            self.__ySupizquierdo=restar
            self.__yInfderecho=restar1
        else:
            print("no se puede realizar la operacion")
    def bajar(self,despB=0):
        sumar=self.__yInfderecho+despB
        if(sumar<=500):
            sumar=self.__ySupizquierdo+despB
        else:
            print("no se puede realizar la operacion")
    def funcionTest(self):
        print("Funcion test:")
        ventana=Ventana('test',30,20,300,300)
        print("Metodo mostrar")
        ventana.mostrar()
        print("Metodo getTitulo:")
        print (ventana.getTitulo())
        print("Metodo alto:")
        print(ventana.alto())
        print("Metodo ancho:")
        print(ventana.ancho())
        print("Metodo moverDerecha")
        ventana.moverDerecha()
        print("Metodo moverIzquierda")
        ventana.moverIzquierda()
        print("Metodo subir")
        ventana.subir()
        print("Metodo bajar")
        ventana.bajar()