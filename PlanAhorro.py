class PlanAhorro:
    __codigoPlan=0
    __modelo=''
    __version=''
    __valor=0.0
    __cantidadCuotasPlan=60
    __cantidadCuotasPagas=10
    def __init__(self,codigoPlan=0,modelo='',version='',valor=0.0):
        self.__codigoPlan=codigoPlan
        self.__modelo=modelo
        self.__version=version
        self.__valor=valor
    @classmethod
    def setCantidadCuotasPlan(cls,cuotas):
        cls.__cantidadCuotasPlan=cuotas
    @classmethod
    def setCantidadCuotasPagas(cls,cuotasPagas):
        cls.__cantidadCuotasPagas=cuotasPagas  
    def getCodigo(self,cod):
        return cod==self.__codigoPlan 
    @classmethod
    def getCuotasPagas(cls):
        return cls.__cantidadCuotasPagas
    def __str__(self):
        return "Codigo:%d,Modelo:%s,Version:%s"%(self.__codigoPlan,self.__modelo,self.__version)
    def modificarPrecio(self,valorA):
        self.__valor=valorA
    def getPrecio(self):
        return self.__valor 
    @classmethod 
    def getCuotasPlan(cls):
        return cls.__cantidadCuotasPlan
    def calcularValor(self):
        return (self.__valor/self.getCuotasPlan())+(self.__valor*0.10)
    def calcularMonto(self):
        return (self.getCuotasPagas()*self.calcularValor())
    def funcionTestPlanAhorro(self):
        print("Funcion Test PlanAhorro:")
        plan1=PlanAhorro(200,'Hilux','4x4 D/C',5322000)
        print(plan1)
        print("Metodo modificarPrecio()")
        plan1.modificarPrecio(3000500)
        print("Metodo getPrecio")
        print(plan1.getPrecio())
        print("Metodo setCantidadCuotasPagas()")
        plan1.setCantidadCuotasPagas(20)
        print("Metodo getCodigo()")
        plan1.getCodigo(200)
        print("Metodo getCuotasPagas()")
        print(PlanAhorro.getCuotasPagas())
        print("Metodo getcCuotasPlan()")
        print(PlanAhorro.getCuotasPlan())
        print("Metodo calcularValor()")
        print(plan1.calcularValor())
        print("Metodo calcularMonto()")
        print(plan1.calcularMonto())
        

