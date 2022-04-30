from ManejadorPlan import ManejadorPlanAhorro
from Menu import Menu
if __name__=='__main__':
    manejador=ManejadorPlanAhorro()
    manejador.cargarArchivo()
    menu=Menu()
    menu.lanzarMenu(manejador)
    