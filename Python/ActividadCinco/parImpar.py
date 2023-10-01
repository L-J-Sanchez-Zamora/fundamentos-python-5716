"""Ingresando un número, decir si es par o impar."""

print("\n❤ Par o Impar❤\n")
while True:
    num = input("Ingresa un número: ")

    if num.isdigit() or (num[0] == '-' and num[1:].isdigit()):
            num = int(num)
            if  num % 2 == 0 or num == 0:
                print(f"\nEl número {num} es un número par.\n")
            else:
                print(f"\nEl número {num} es número impar.\n")
    else:
            print("\n⚠️  Los números pares o impares son enteros ⚠️\n*****Por favor ingresa un número entero*****\n")

