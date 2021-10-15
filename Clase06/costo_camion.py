#costo_camion
from informe_funciones import leer_camion

def costo_camion(ruta):
    total = 0
    record = leer_camion(ruta)
    for linea in record:
        try:
            ncajones = int(linea['cajones'])
            precio = float(linea['precio'])
            total += ncajones * precio
        except ValueError:
            print("Error: falta un dato o no es un número")
    return(total)

total = costo_camion('../Data/camion.csv')
print('Costo total:', total)