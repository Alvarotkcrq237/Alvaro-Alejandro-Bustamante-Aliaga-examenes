"""EJERCICIO 2:
2. Usando el concepto de herencia y encapsulación (para el atributo saldo)
para crear elsiguiente programa (3 ptos):
Reglas:
    - Crear una clase llamada Persona y agregar un atributo saldo a esta clase
    (ejercicio anterior).
    - Crear un método transferencia y mostrar saldo (mostrará el saldo actual
    que tiene la persona) para la clase mencionada
    - El método transferencia hace que la clase Empleado que llame al método
    pueda transferir la cantidad monto al objeto Empleado2 por consiguiente
    deberá ir actualizando también el saldo o monto que tiene el otro empleado
    en su cuenta cada vez que use el método transferencia
    - Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
    imprimir “Saldo insuficiente”. Comprobar instanciado la clase realizando
    una transferencia y con dos personas.
"""

class persona:
    def guardar_saldo(self, monto):
        self.__saldo = monto

    def mostrar_saldo(self):
        print("{} tiene S/ {:.2f} de saldo.".format(self.nombre, self.__saldo))

    def transferir_a(self, monto, receptor):
        if self.__saldo >= monto:
            self.__saldo -= monto
            receptor.__saldo += monto
            print("se transfirió S/ {:.2f} de {} a {}".format(monto, self.nombre, receptor.nombre))
        else:
            print("saldo insuficiente")


class empleado(persona):
    def registrar(self, codigo):
        print("---> datos del empleado {} <---".format(codigo))
        self.nombre = input("ingrese el nombre del empleado {}: ".format(codigo))
        self.edad = int(input("ingrese la edad del empleado {}: ".format(codigo)))
        self.ingresos = float(input("ingrese el sueldo del empleado {}: ".format(codigo)))
        self.pais = "peruana"
        saldo_inicial = float(input("ingrese el saldo inicial de {}: ".format(self.nombre)))
        self.guardar_saldo(saldo_inicial)

    def obtener_nombre(self):
        return self.nombre

    def obtener_edad(self):
        return self.edad

    def subir_ingresos(self):
        self.ingresos *= 1.30


# empleados
trab1 = empleado()
trab1.registrar(1)

trab2 = empleado()
trab2.registrar(2)

# sueldos
print("\nsueldo original de {}: {:.2f}".format(trab1.obtener_nombre(), trab1.ingresos))
print("sueldo original de {}: {:.2f}".format(trab2.obtener_nombre(), trab2.ingresos))

trab1.subir_ingresos()
trab2.subir_ingresos()

print("\nsueldo actualizado de {}: {:.2f}".format(trab1.obtener_nombre(), trab1.ingresos))
print("sueldo actualizado de {}: {:.2f}".format(trab2.obtener_nombre(), trab2.ingresos))

# transferencias
while True:
    print("\n--- transferencia ---")
    quien = input("quién transfiere ({} o {}): ".format(trab1.nombre, trab2.nombre)).lower()

    if quien == trab1.nombre.lower():
        emisor = trab1
        receptor = trab2
    elif quien == trab2.nombre.lower():
        emisor = trab2
        receptor = trab1
    else:
        print("nombre no válido")
        continue

    monto = float(input("cuánto quieres transferir de {} a {}: ".format(emisor.nombre, receptor.nombre)))
    emisor.transferir_a(monto, receptor)

    trab1.mostrar_saldo()
    trab2.mostrar_saldo()

    seguir = input("¿quieres hacer otra transferencia? (si o no): ").lower()
    if seguir != "si":
        break




