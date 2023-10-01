#Opc sin while: Pedir 3 datos por teclado y almacenarlos en una lista               
"""
dato1=int(input("Ingresa primer dato: "))
dato2=int(input("Ingresa segundo dato: "))
dato3=int(input("Ingresa tercer dato: "))
newArray=[dato1,dato2,dato3]
print (newArray)
"""

#Opc usando while True. Usando el ciclo While,pedir 3 datos por teclado y almacenarlos en una lista

while True:
    dato1=input("Ingresa primer dato: ")
    dato2=input("Ingresa segundo dato: ")
    dato3=input("Ingresa tercer dato: ")
    newArray=[dato1,dato2,dato3]
    print (newArray)
    break

# Usando el ciclo While,pedir 3 datos por teclado y almacenarlos en una lista
"""
lista=[]
# Define una variable para contar cuántos datos se han ingresado.
contador = 0
# Establece la cantidad máxima de datos que deseas ingresar (en este caso, 3).
x = 3

while contador < x:
    dato=input("Ingresa dato: ")
    lista.append(dato)
    contador += 1
    print(lista)
"""

