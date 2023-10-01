#Actividad 4
#Ejercicio3

#Sumar los números desde la posición 6 hasta la 9 en una lista de 10 elementos
numeros=[1,2,3,4,5,6,7,8,9,10]

posi=6
total=0

for num in numeros:
    total=total+numeros[posi]
    posi=posi+1
    if posi==9:
        break
print(total)