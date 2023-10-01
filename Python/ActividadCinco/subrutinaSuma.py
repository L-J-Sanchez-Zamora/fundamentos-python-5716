"""Crear una subrutina para sumar dos números que se digitan por teclado"""

print("Suma")

def suma (num1,num2):
    return num1+num2

num1=int(input("Ingresa primer dato: "))
num2=int(input("Ingresa segundo dato: "))
resultado=suma(num1,num2)
print("El resultado de la suma es: ", resultado)

