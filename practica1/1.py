#EJERCICIO 1
nombre = "Alvaro"
salario = 5000
edad = "20"
compañia = "AyG Industrias"
print("Tipo de nombre:", type(nombre))
print("Tipo de salario:", type(salario))
print("Tipo de edad:", type(edad))
print("Tipo de compañía:", type(compañia))

edad_convertida = int(edad)
print("Tipo de edad_convertida:", type(edad_convertida))

print("_______________________________________________________")

if (edad_convertida > 30):
    print("Usted tiene un bono de 10% en el mes de diciembre")
    bono_1 = salario * 0.10

if (edad_convertida < 30):
    print("Usted tiene un bono del 5% en el mes diciembre")
    bono_1 = salario * 0.05

bono_final = (pow(salario,2)) + bono_1
print(f"El bono final es: {bono_final}")