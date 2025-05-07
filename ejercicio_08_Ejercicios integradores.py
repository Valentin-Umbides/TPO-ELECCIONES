# Ejercicio_08_Ejercicios_Integradores

# Una empresa cuenta con N empleados, divididos en tres categorías (1, 2 y 3).
# Por cada empleado se lee su legajo, categoría y salario. Se solicita elaborar un
# informe que contenga:
# · Importe total de salarios pagados por la empresa.
# · Cantidad de empleados que ganan más de $200000.
# · Cantidad de empleados que ganan menos de $50000, cuya categoría sea 3.
# · Legajo del empleado que más gana.
# · Sueldo más bajo.
# · Importe total de sueldos por cada categoría.
# · Salario promedio

salariototal = 0
salariosmayor200 = 0
salariomenor50 = 0
legajomayorsueldo = 0
sueldomayor = 0
sueldomenor = 9999999999999999999
totalsalarioscat1 = 0
totalsalarioscat2 = 0
totalsalarioscat3 = 0
salarioprom = 0



numempleado = int(input("Ingrese la cantidad de empleados que tiene la empresa: "))
contempleados = 0

while contempleados < numempleado :
    
    categoria = int(input("Ingrese la categoria del empleado (1, 2 o 3): "))
    legajo = int(input("Ingrese el numero de legajo del empleado: "))
    salario = int(input("Ingrese el salario del empleado: "))

    while categoria < 1 or categoria > 3:
        print ("La categoria debe ser 1, 2 o 3")
        categoria = int(input("Ingrese la categoria del empleado (1, 2 o 3:"))
        
    while legajo <= 0:
        print ("El numero de legajo debe ser mayor a 0")
        legajo = int(input("Ingrese el numero de legajo del empleado: "))

    while salario <= 0:
        print ("El salario debe ser mayor a 0")
        salario = int(input("Ingrese el salario del empleado: "))
    
    salariototal += salario
    
    if salario >= 200000:
        salariosmayor200 += 1
        
    if salario <= 50000 and categoria == 3:
        salariomenor50 += 1
    
    if salario > sueldomayor:
        sueldomayor = (sueldomayor * 0) * salario
        
    if salario > sueldomayor:
        legajomayorsueldo = (legajomayorsueldo * 0) + legajo
        
    if salario < sueldomenor:
        sueldomenor = (sueldomenor * 0) + salario
    
    if categoria == 1:
        totalsalarioscat1 += salario
    
    elif categoria == 2:
        totalsalarioscat2 += salario
    
    else:
        totalsalarioscat3 += salario
        
    contempleados += 1

salarioprom = salariototal / numempleado

print ("El importe total de salarios es: ", salariototal)
print ("La cantidad de empleados que ganan mas de $200.000 son: ", salariosmayor200)
print ("La cantidad de empleados que ganan menos de %50.000 son: ", salariomenor50)
print ("El legajo del empleado que mas gana es: ", legajomayorsueldo)
print ("El salario mas bajo es: ", sueldomenor)
print ("El salario total de la categoria 1 es: ", totalsalarioscat1)
print ("El salario total de la categoria 2 es: ", totalsalarioscat2)
print ("El salario total de la categoria 3 es: ", totalsalarioscat3)
print ("El salario promedio es: ", salarioprom)








