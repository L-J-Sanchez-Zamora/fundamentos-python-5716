"""nota1 =float(input("Ingrese primera nota: "))
nota2 =float(input("Ingrese segunda nota: "))
nota3 =float(input("Ingrese tercera nota: "))

total = (nota1 + nota2 + nota3) / 3


if 1 <= nota1 <= 10 and 1 <= nota2 <= 10 and 1 <= nota3 <=10 :
    if   total >= 9 : print("Felicitaciones")
    elif total >=8 and total <= 8.9 : print("Buen trabajo")
    elif total >=6 and total <= 7.9 : print("Regular")
    elif total >=4 and total <= 5.9 : print("Malo")
    elif total < 4 : print("Muy malo")
else:
    print("Error las notas deben estar entre 1 y 10")"""

nota1 =float(input("Ingrese primera nota: "))
nota2 =float(input("Ingrese segunda nota: "))
nota3 =float(input("Ingrese tercera nota: "))

total = (nota1 + nota2 + nota3) / 3

if 1 <= nota1 <= 10 and 1 <= nota2 <= 10 and 1 <= nota3 <=10 :    
    if   total >= 9: 
     mensaje="Felicitaciones"
    elif 8>= total<= 8.9:
     mensaje="Buen trabajo"
    elif 6>= total <= 7.9 : 
     mensaje="Regular"
    elif 4>=  total <= 5.9 : 
     mensaje="Malo"
    else:
     mensaje="Muy malo"
    print("La nota promedio es: ", total)
    print("Mensaje: ", mensaje)
            
else:
        print("Error el numero debe estar esntre 1 y 10")


