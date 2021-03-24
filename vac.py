print("Programa de calculo de vacaciones de Rappi\n")
nombre = input("cual es tu nombre?: ")

clave = int(input("Cual es tu clave?: "))

años = float(input("Numero de años trabajados?: "))

if clave == 1:
    if años >= 1 and años < 2:
        print("el empleado ", nombre, " tiene derecho a 6 dias de vacaciones")
    elif años >=2 and años <= 6:
        print("el empleado ", nombre, " tiene derecho a 14 dias de vacaciones")
    elif años >= 7:
        print("el empleado ", nombre, " tiene derecho a 20 dias de vacaciones")
    else:
        print("el empleado ", nombre, " aun no tiene derecho a 6 dias de vacaciones")

elif clave == 2:
    if años >= 1 and años < 2:
        print("el empleado ", nombre, " tiene derecho a 7 dias de vacaciones")
    elif años >=2 and años <= 6:
        print("el empleado ", nombre, " tiene derecho a 15 dias de vacaciones")
    elif años >= 7:
        print("el empleado ", nombre, " tiene derecho a 22 dias de vacaciones")
    else:
        print("el empleado ", nombre, " aun no tiene derecho a 6 dias de vacaciones")
    

elif clave == 3:
    if años >= 1 and años < 2:
        print("el empleado ", nombre, " tiene derecho a 10 dias de vacaciones")
    elif años >=2 and años <= 6:
        print("el empleado ", nombre, " tiene derecho a 20 dias de vacaciones")
    elif años >= 7:
        print("el empleado ", nombre, " tiene derecho a 30 dias de vacaciones")
    else:
        print("el empleado ", nombre, " aun no tiene derecho a 6 dias de vacaciones")

else:
    print("la clave no existe")

print("Gracias por usar el sistema de rappi")