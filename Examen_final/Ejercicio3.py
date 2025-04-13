"""EJERCICIO 3:
3. (3 ptos) Crear un programa usando decoradores para mostrar solo la hora
y el minuto del momento que se usa el decorador
Reglas:
- Al ejecutar el decorador mostrará un mensaje: “El decorador está siendo
ejecutado a las H con minutos”
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo: usando 6 números e indicar el mayor de
todos ellos (o x números) para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**) y visualizar los resultados usando el decorador implementado
con un mínimo tres ejemplos.
"""
import datetime


def funcion_decoradora(func):
    def fun2(*args, **kwargs):
        h = datetime.datetime.now().hour
        m = datetime.datetime.now().minute
        print("El decorador esta siendo ejecutado "
              "a las {} con minutos {}".format(h, m))
        return func(*args, **kwargs)
    return fun2


@funcion_decoradora
def numero_mayor(*nums):
    return max(nums)


rpta1 = numero_mayor(10, 20, 30, 40, 50, 60)
print("El numero mayor es: {}".format(rpta1))
print("La suma de los numeros es: {}".format(sum([10, 20, 30, 40, 50, 60])))
print("----------------------------------------------------------")

rpta2 = numero_mayor(5, 15, 25, 35, 45)
print("El numero mayor es: {}".format(rpta2))
print("La suma de los numeros es: {}".format(sum([5, 15, 25, 35, 45])))
print("----------------------------------------------------------")

rpta3 = numero_mayor(7, 14, 21, 28)
print("El numero mayor es: {}".format(rpta3))
print("La suma de los numeros es: {}".format(sum([7, 14, 21, 28])))
print("----------------------------------------------------------")

rpta4 = numero_mayor(17, 74, 21, 38)
print("El numero mayor es: {}".format(rpta4))
print("La suma de los numeros es: {}".format(sum([17, 74, 21, 38])))
print("----------------------------------------------------------")
