""" EJERCICIO 1:
1. Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:
    - Crear una clase llamada Empleado donde sus atributos deben ser nombre,
    edad, saldo y de nacionalidad peruana, tendrá un método para solicitar su
    nombre y otro para solicitar su edad.
    - Tendrá un método cumpleaños donde cada vez que invoque aumentará en
    un año la edad de la persona.
    - Crear la instancia de la clase Persona y usar su nuevo método
    aumentoSueldo para incrementar su sueldo en un 30% (mínimo instanciar
    la clase 2 veces, mostrar por pantalla dicho sueldo ya incrementado).
    - Crear un siguiente método que retorne un mensaje donde indique que: “En
    el año 2025 tendrá XX años”, el año se ingresará por parámetro y la edad
    es la edad que ya se ingresó (Mostrar por pantalla este valor)
"""
class empleado:
    def registrar(self, codigo):
        print("---> Datos del empleado {} <---".format(codigo))
        self.nombre = input("ingrese el nombre del empleado {}: ".format(codigo))
        self.edad = int(input("ingrese la edad del empleado {}: ".format(codigo)))
        self.ingresos = float(input("ingrese el sueldo del empleado {}: ".format(codigo)))
        self.pais = "peruana"
    def obtener_nombre(self):
        return self.nombre
    def obtener_edad(self):
        return self.edad
    def subir_ingresos(self):
        self.ingresos *= 1.30
    def edad_proyectada(self, anio, edad_dada):
        if edad_dada < self.edad:
            print("no se puede calcular. la edad es menor a la actual.")
        else:
            print("en el año {} tendrá {} años.".format(anio, edad_dada))

trab1 = empleado()
trab1.registrar(1)

trab2 = empleado()
trab2.registrar(2)

print("\nsueldo original de {}: {:.4f}".format(trab1.obtener_nombre(), trab1.ingresos))
print("sueldo original de {}: {:.4f}".format(trab2.obtener_nombre(), trab2.ingresos))

trab1.subir_ingresos()
trab2.subir_ingresos()

print("\nsueldo actualizado de {}: {:.4f}".format(trab1.obtener_nombre(), trab1.ingresos))
print("sueldo actualizado de {}: {:.4f}".format(trab2.obtener_nombre(), trab2.ingresos))

anio_futuro = int(input("\naño a proyectar: "))

edad1 = int(input("edad futura de {} en {}: ".format(trab1.nombre, anio_futuro)))
trab1.edad_proyectada(anio_futuro, edad1)

edad2 = int(input("edad futura de {} en {}: ".format(trab2.nombre, anio_futuro)))
trab2.edad_proyectada(anio_futuro, edad2)





