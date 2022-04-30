import csv
from PlanAhorro import PlanAhorro
class ManejadorPlanAhorro:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    
    def agregarPlan(self,plan):
        if type(plan)==PlanAhorro:
            self.__lista.append(plan)
        else:
            print("No se puede cargar")
    def cargarArchivo(self):
        archivo=open("planes.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True
        for fila in reader:
            
            if bandera:
                bandera=not bandera
                PlanAhorro.setCantidadCuotasPlan(int(fila[4]))
                PlanAhorro.setCantidadCuotasPagas(int(fila[5]))
            self.agregarPlan(PlanAhorro(int(fila[0]),fila[1],fila[2],float(fila[3])))
        archivo.close()
    #punto5.1
    def modificarValorVehiculo(self):
        for i in range(len(self.__lista)): 
            print(self.__lista[i])  
            valorActual=float(input("Ingrese el valor actual:"))
            self.__lista[i].modificarPrecio(valorActual)
    #punto5.2
    def mostrarVehiculos(self,valorV):
        for i in range(len(self.__lista)):
            if self.__lista[i].calcularValor()<valorV:
                print(self.__lista[i])
    def buscarCodigoPlan(self,cod):
        i=0
        lon=len(self.__lista)
        bandera=True
        while i<lon and bandera:
            if self.__lista[i].getCodigo(cod):
                bandera= False
            else:
                i+1
        resultado=0        
        if bandera:
            resultado=-1
        else:
            resultado=i
        return resultado
    def mostrarMontosVehiculos(self,pos):
        if pos==-1:
            print("No se encontro el plan")
        else:
            print("El monto para licitar es:{}".format(self.__lista[pos].calcularMonto()))
    def funcionTest(self):
        print("Funcion test ManejadorPlan:")
        manejador1=ManejadorPlanAhorro()
        print("Metodo agregarPlan():")
        manejador1.agregarPlan(PlanAhorro(150,'Volkwagen','Trendline',2653900))
        print("Metodo cargarArchivo()")
        manejador1.cargarArchivo()
        print("Metodo mostrarVehiculos():")
        manejador1.mostrarVehiculos(5000000)
        print("Metodo buscarCodigoPlan():")
        pos=manejador1.buscarCodigoPlan(150)
        print("Metodo mostrarMontosVehiculos():")
        manejador1.mostrarMontosVehiculos(pos)