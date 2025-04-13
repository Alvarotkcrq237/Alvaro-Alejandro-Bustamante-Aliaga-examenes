""" EJERCICIO 1:
1. Utilizar el concepto de módulo necesariamente. Escribir un programa para
el manejo de listas el cuál cumplirá los siguientes requerimientos (4 ptos):
Reglas:
- Crear una función que le permitirá almacenar 10 números aleatorios en una
lista y finalmente los imprimirá por consola al llamar la función.
- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.
- Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
consola.
- Crear una función para indicar cuál es mayor número par de la lista (lista
del ítem 2), retornar este valor e imprimirlo por consola.
- Crear el archivo principal.py, donde solo llamarás las anteriores
funciones que se encontrarán alojadas en un módulo
"""
import random


def creador_lista():
    lis1 = []
    for i in range(10):
        lis1.append(random.randint(1, 200))
    return lis1


def quitar_repe(lis1):
    lis2 = []
    for num in lis1:
        if num not in lis2:
            lis2.append(num)
    return lis2


def ordenamiento(lis2):
    lis3 = sorted(lis2)
    lis4 = sorted(lis2, reverse=True)
    return lis3, lis4


def parmayor(lis2):
    pares = []
    for num in lis2:
        if num % 2 == 0:
            pares.append(num)
    if pares:
        return max(pares)
    else:
        return 0
