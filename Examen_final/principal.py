"""Continuacion del EJERCICIO 1"""
from Ejercicio1_modulos import (creador_lista, quitar_repe,
                                ordenamiento, parmayor)

lista = creador_lista()
print("Lista generada:", lista)

sin_repe = quitar_repe(lista)
print("Lista sin repetidos:", sin_repe)

menor, mayor = ordenamiento(sin_repe)
print("Orden de menor a mayor:", menor)
print("Orden de mayor a menor:", mayor)

mayor_par = parmayor(sin_repe)
if mayor_par == 0:
    print("No hay números pares.")
else:
    print("Mayor número par:", mayor_par)
