
def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        invertida.insert(0,e) #agrego el elemento e al principio de la lista invertida
    return invertida

def main():
    print(invertir_lista([1, 2, 3, 4, 5]))
    print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))