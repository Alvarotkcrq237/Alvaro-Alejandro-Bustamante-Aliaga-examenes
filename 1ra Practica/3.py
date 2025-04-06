nombre = "Álvaro"
apellido = "Gómez"
salario = 7500
edad = "32"
compania = "Universidad de Ingeniería y Tecnología"

edad_convertida = int(edad)

if edad_convertida > 30:
    print("Usted tiene un bono de 10% en el mes de diciembre")
    bono_1 = salario * 0.10
else:
    print("Usted tiene un bono del 5% en el mes diciembre")
    bono_1 = salario * 0.05

bono_final = (pow(salario, 2)) + bono_1
print(f"El bono final es: {bono_final}")

datos_trabajador = []
datos_trabajador.append(nombre)
datos_trabajador.append(apellido)
datos_trabajador.append(salario)
datos_trabajador.append(edad_convertida)
datos_trabajador.append(compania)
datos_trabajador.append(bono_final)

trabaja_actualmente = True
datos_trabajador.append(trabaja_actualmente)

hijos = 2  # Cambia este valor si quieres modificar el número de hijos

if hijos > 0:
    bono_familiar = salario * 0.08
    print(f"Obtiene el bono familiar el cuál es de: {bono_familiar}")
    datos_trabajador.append(bono_familiar)
else:
    print("No cumple para obtener el bono familiar")
    datos_trabajador.append("No cumple para obtener el bono familiar")

print("Lista actualizada con el bono familiar:", datos_trabajador)
print("Tamaño de la lista:", len(datos_trabajador))

if trabaja_actualmente:
    print(f"El trabajador {nombre} {apellido} se encuentra trabajando actualmente en la compañía.")
else:
    print(f"El trabajador {nombre} {apellido} ya no se encuentra trabajando actualmente en la empresa.")
