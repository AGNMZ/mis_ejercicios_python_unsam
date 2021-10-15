#%% Ejercicio 4.6 // Propagacion

def propagar(Lista):
    # vector=[]
    # for pos,fosforo in enumerate(Lista) :
    #     if pos==0:
    #         if Lista[pos+1] != 1:
    #             vector.append(fosforo)
    #         else:
    #             vector.append(1)
    #     if pos==-1:
    #         if Lista[pos-1] != 1:
    #             vector.append(fosforo)
    #         else:
    #             vector.append(1)
    #     if pos != 0 and pos != -1:
    #         if fosforo == -1 or fosforo == 1:
    #             vector.append(fosforo)
    #         else:
    #             if Lista[pos-1] == 1 or Lista[pos+1] == 1:
    #                 vector.append(1)  
    #             else:
    #                 vector.append(fosforo) 
        
    # invertida=[] 
    # for e in vector:
    #     invertida  = [e] + invertida
    
    secuencia=[]
    for pos,fosforo in enumerate(Lista) :
        if pos==0:
            if Lista[pos+1] != 1:
                secuencia.append(fosforo)
            else:
                secuencia.append(1)
        if pos==-1:
            if Lista[pos-1] != 1:
                secuencia.append(fosforo)
            else:
                secuencia.append(1)
        if pos != 0 and pos != -1:
            if fosforo == -1 or fosforo == 1:
                secuencia.append(fosforo)
            else:
                if Lista[pos-1] == 1 or Lista[pos+1] == 1:
                    secuencia.append(1)  
                else:
                    secuencia.append(fosforo)
    return secuencia  

lista_1 = [ 0, 0, 0, 1, 0, 0]
lista_2 = [ 0, 0, 0, 0, 0, -1]
lista_3 = [ 0, 0, 0, 0, 0, 1]
lista_4 = []
lista_5 = [ 0 for _ in range(1000) ] + [1]
lista_6 = [1] + [ 0 for _ in range(1000) ]
lista_7 = [ (i% 6)//2-1 for i in range(200) ]
lista_8 = [ -1*((i% 6)//2-1) for i in range(60) ]
# print(lista_1)
# print(propagar(lista_1))
# print(lista_2)
# print(propagar(lista_2))
print(lista_3)
print(propagar(lista_3))
# print(lista_4)
# print(propagar(lista_4))
# print(lista_5)
# print(propagar(lista_5))
# print(lista_6)
# print(propagar(lista_6))
# print(lista_7)
# print(propagar(lista_7))
# print(lista_8)
# print(propagar(lista_8))