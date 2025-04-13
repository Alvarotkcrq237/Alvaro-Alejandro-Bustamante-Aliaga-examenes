"""EJERCICIO 2:
2. (3 ptos) Crear un decorador conteo.
Reglas:
- El decorador retornará la cantidad de parámetros que hayas usado en la
función y que a su vez evaluará que deba ser mayor que 1 para procesar esta
lógica, caso contrario indicarlo con un mensaje respectivamente.
- Al final de la función decorada indicará mediante un mensaje que la función
fue ejecutada.
- La función que vas a crear va a capturar, la edad, nombre, hora y minuto en
que fue registrado la persona (usar la librería correspondiente)
Mostrando un mensaje siguiente: “Pedro de 30 años ha sido registrado a las
16 horas con 20 minutos”
- La que función que será decorada calculará la media de 4 notas.
"""
import datetime


def fun_decorador(fun1):
    def fun2(*args, **kwargs):
        total = len(args) + len(kwargs)
        if total > 1:
            rpta = fun1(*args, **kwargs)
            print("función ejecutada")
            return rpta
        else:
            print("tienes que poner mas de un dato")
    return fun2


@fun_decorador
def registro(nombre, edad, n1, n2, n3, n4):
    prom = (n1 + n2 + n3 + n4) / 4
    tiempo = datetime.datetime.now()
    h = tiempo.hour
    m = tiempo.minute
    print("{} de {} años fue registrado a las {} horas con {} minutos.".format(
        nombre, edad, h, m))
    print("su promedio fue: {:.3f}".format(prom))


registro("Alvaro", 20, 15, 17, 18, 17)
