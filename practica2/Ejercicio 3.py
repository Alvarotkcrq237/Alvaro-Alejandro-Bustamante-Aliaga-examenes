""" EJERCICIO 3:
3. Escribir un programa para gestionar una billetera electrónica (3 ptos):
Reglas:
    - El programa deberá considerar 2 cuentas bancarias: 1 en soles y
    otra en dólares. Considerar el nombre y apellido del titular
    - Deberá tener un método para transferir entre sus cuentas, pero
    para realizar esto debe hacer una conversión de monedas.
    - Tendrá otro método para retirar dinero, esto debe actualizar ambas
    cuentas y mostrar en pantalla los montos actualizados, a su vez
    validar si tiene fondos suficientes o no para el retiro, mostrar un
    mensaje que indique no tiene suficientes en caso fuera el caso.
    - Instanciar 3 veces los casos de transferencias para ver reflejado el
    uso de tus métodos creados.
"""

print("===> Bienvenido a tu billetera electrónica <===")
nombre = input("Nombre del titular: ")
apellido = input("Apellido del titular: ")

soles = float(input("Saldo en soles: s/"))
dolares = float(input("Saldo en dólares: $"))

cambio = 3.66

print("\n--- TRANSFERENCIAS ---")
n = 1
while n <= 3:
    print("\nTransferencia", n)
    print("1. Soles a dólares")
    print("2. Dólares a soles")
    op = input("Opción: ")

    if op == "1":
        m = float(input("Monto en soles: "))
        if soles >= m:
            soles -= m
            dolares += m / cambio
            print("Hecho.")
        else:
            print("No hay saldo.")
    elif op == "2":
        m = float(input("Monto en dólares: "))
        if dolares >= m:
            dolares -= m
            soles += m * cambio
            print("Hecho.")
        else:
            print("No hay saldo.")
    else:
        print("Opción inválida.")

    print("Soles: S/ {:.2f}".format(soles))
    print("Dólares: $ {:.2f}".format(dolares))
    n += 1

print("\n--- RETIRO ---")
print("1. Retirar soles")
print("2. Retirar dólares")
r = input("Opción: ")

if r == "1":
    monto = float(input("Cuánto quiere retirar en soles: "))
    if soles >= monto:
        soles -= monto
        print("Retiro hecho.")
    else:
        print("No hay saldo.")
elif r == "2":
    monto = float(input("Cuánto quiere retirar en dólares: "))
    if dolares >= monto:
        dolares -= monto
        print("Retiro hecho.")
    else:
        print("No hay saldo.")
else:
    print("Opción inválida.")

print("\n---> SALDO FINAL <---")
print("Titular:", nombre, apellido)
print("Soles: S/ {:.4f}".format(soles))
print("Dólares: $ {:.4f}".format(dolares))

