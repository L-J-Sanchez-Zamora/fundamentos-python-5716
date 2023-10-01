"""Actividad de Entrega
Realizar una calculadora usando sub-rutinas. Se introduce un número de 1 a 4.

Si es el número 1 se llama la subrutina de sumar.
Si es el número 2 se llama la subrutina de restar.
Si es el número 3 se llama la subrutina de multiplicar.
Si es el número 4 se llama la subrutina de dividir.
En los 4 casos se piden por pantalla 2 números.
El número de 1 a 4 para las operaciones, si es diferente, mostrar “número equivocado”
Nota: Crear el código, copiarlo y pegarlo en un documento de Word y mostrar un pantallazo de los 4 resultados (uno por cada operación) cargar la actividad a través de "Envío actividad 5" para ser evaluada. """
#SUBRUTINAS#
def suma(num1,num2):
    return num1+num2
def resta(num1,num2):
    return num1-num2
def multiplicacion(num1,num2):
    return num1*num2
def division(num1,num2):
        if num2 == 0:
            print("⛔ Error: No es posible dividir entre 0 ⛔ ")
            return None
        return num1/num2
#COD PRINCIPAL#

while True:
    print("\n☑️  Calculadora ☑️\n")
    print("1. Suma ➕")
    print("2. Resta ➖")
    print("3. Multiplicación ✖️")
    print("4. Dividición ➗")
    print("5. Salir ❎")
    dato = int(input("\nIngresa el número de la operación que desea usar: "))

    if dato==5:
         print("Saliendo de la calculadora")
         break
    
    elif dato == 1:
        num1=int(input("Ingresa primer dato: "))
        num2=int(input("Ingresa segundo dato: "))
        resultado=suma(num1,num2)
        print("El resultado de la suma es: ", resultado)

    elif dato == 2:
        num1=int(input("Ingresa primer dato: "))
        num2=int(input("Ingresa segundo dato: "))
        resultado=resta(num1,num2)
        print("El resultado de la resta es: ",resultado)

    elif dato == 3:
        num1=int(input("Ingresa primer dato: "))
        num2=int(input("Ingresa segundo dato: "))
        resultado=multiplicacion(num1,num2)
        print("El resultado de la multiplicación es: ",resultado)

    elif dato == 4:
        num1=int(input("Ingresa primer dato: "))
        num2=int(input("Ingresa segundo dato: "))
        resultado=division(num1,num2)
        if resultado is not None:
            print("El resultado de la división es: ",resultado)

    else:
        print("Ingrese una opcion valida")