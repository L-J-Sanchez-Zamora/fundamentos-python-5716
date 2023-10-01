#Actividad 4
#Ejercicio1

ciudad = str(input("Ingrese nombre de la ciudad: "))
edad = int(input("Ingrese su edad: "))

#Si vive en Bogotá o Cali y tiene entre 18 y 30 años colocar como

if (ciudad =="Bogotá" or ciudad =="Cali") and (18 <= edad <=30) :
    #respuesta “super”, sino colocar como respuesta “bien”. 

    print("super")
else:
    print("bien")