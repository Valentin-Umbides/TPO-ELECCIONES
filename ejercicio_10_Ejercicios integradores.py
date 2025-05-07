# Ejercicio_10_Ejercicios_Integradores

# Consigna:

# Un complejo de cines necesita un programa para contabilizar el dinero que recauda.
# Por cada función se ingresa la cantidad de espectadores y si esa función
# tiene descuento o no (1=Sí, 2=No). La carga finaliza cuando la cantidad de espectadores
# sea igual a cero. En ese momento el programa deberá:
# · Calcular la recaudación total del complejo, considerando que el valor de la
# entrada es de $3500 en los días de descuento $5000 en los días sin
# descuento.
# · Determinar cuántos espectadores ingresaron con descuento y qué
# porcentaje representan sobre el total de funciones.

espectadores = int(input("Indique la cantidad de espectadores que tuvo la funcion (0 para finalizar el programa): "))
total = 0
especdesc = 0
totalespec = 0

while espectadores != 0:
    
    while espectadores < 0:
        print ("La cantidad de espectadores no puede ser menor a 0.")
        espectadores = int(input("Indique la cantidad de espectadores que tuvo la funcion (0 para finalizar el programa: "))

    descuento = int(input("La funcion tuvo descuento (1 = SI, 2 = NO)? "))
    
    while descuento != 1 and descuento != 2:
        print ("ERROR!")
        descuento = int(input("Inidique si la funcion tuvo descuento (1 = SI, 2 = NO)"))
    
    if descuento == 1:
        total += 3500 * espectadores
        especdesc += espectadores
        totalespec += espectadores
    
    else:
        total += 5000 * espectadores
        totalespec += espectadores
        
    espectadores = int(input("Indique la cantidad de espectadores que tuvo la funcion (0 para finalizar el programa): "))
        
print ("La recaudacion total del complejo fue de: $", total)
print (especdesc, "entraron con descuento, esto cubre un %", (especdesc / totalespec) * 100, "sobre el total de las funciones.")
        