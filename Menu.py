from ManejadorPlan import ManejadorPlanAhorro
from PlanAhorro import PlanAhorro
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '5':self.opcion5,
            '6':self.salir
            }
    def lanzarMenu(self,manejador):
        #Menu opciones
        if type(manejador)==ManejadorPlanAhorro:
            i=str(len(self.__opciones))
            opcion=0
            while(i!=opcion):
                print('Menu:')
                print('-Ingrese 1 para actualizar el valor de cada vehiculo.')
                print('-Ingrese 2 para mostrar el promedio mensual de cada hora.')
                print('-Ingrese 3 para mostrar monto para licitar el vehiculo.')
                print('-Ingrese 4 para mostrar la cantidad de cuotas para licitar.')
                print('-Ingrese 5 para funcion test.')
                print('-Ingrese 6 para salir.')
                opcion=input('Ingrese opcion:\n')
                ejecutar=self.__opciones.get(opcion,self.error)
                if (opcion=='1'or opcion=='2' or opcion=='3' or opcion=='4'or opcion=='5'):
                    ejecutar(manejador)
                else:
                    ejecutar()
    def opcion1(self,manejador):
        manejador.modificarValorVehiculo()
    def opcion2(self,manejador):
        valorV=float(input("Ingrese el valor:"))
        manejador.mostrarVehiculos(valorV)
    def opcion3(self,manejador):
        codigo=int(input("Ingrese el codigo de plan a buscar:"))
        pos=manejador.buscarCodigoPlan(codigo)
        manejador.mostrarMontosVehiculos(pos)
    def opcion4(self,manejador):
        cantidad=(int(input("Ingrese la cantidad para modificar")))
        PlanAhorro.setCantidadCuotasPagas(cantidad)
    def opcion5(self,manejador):
        manejador.funcionTest()
        plan=PlanAhorro()
        plan.funcionTestPlanAhorro()
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')
    