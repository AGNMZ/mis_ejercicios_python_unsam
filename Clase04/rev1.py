#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def propagar(fosforos):
    for i, fosforo in enumerate(fosforos):
        if fosforo == 0:
            try:
                if fosforos[i-1] ==1 or fosforos[i+1] ==1:
                    fosforos[i] = 1
                    for i in range(i,-1,-1):
                        if fosforos[i] != -1:
                            fosforos[i] = 1
                        else:
                            break
            except IndexError:
                pass
    return fosforos


lista_1 = [ 0, 0, 0, 1, 0, 0]
lista_2 = [ 0, 0, 0, 0, 0, -1]
lista_3 = [ 0, 0, 0, 0, 0, 1]
lista_4 = []
lista_5 = [ 0 for _ in range(1000) ] + [-1]
lista_6 = [1] + [ 0 for _ in range(1000) ]
lista_7 = [ (i% 6)//2-1 for i in range(200) ]
lista_8 = [ -1*((i% 6)//2-1) for i in range(60) ]
# print(lista_1)
# print(propagar(lista_1))
# print(lista_2)
# print(propagar(lista_2))
# print(lista_3)
# print(propagar(lista_3))
# print(lista_4)
# print(propagar(lista_4))
print(lista_5)
print(propagar(lista_5))
# print(lista_6)
# print(propagar(lista_6))
# print(lista_7)
# print(propagar(lista_7))
# print(lista_8)
# print(propagar(lista_8))