# Autor: Joshua Sánchez Martínez A01274269
# Divide entre dos numeros y encuentra el numero mayor de una serie de numeros


#Funcion para encontrar el numero mayor
def buscarNumeroMayor():
    print("Teclea una serie de números para encontrar el mayor.")
    numero1 = int(input("Teclea tu numero, -1 para salir"))
    numero2 = -1
    while numero1 != -1:
        if numero1 > numero2:
            numero2 = numero1
        else:
            pass
        numero1 = int(input("Teclea tu numero, -1 para salir"))
    if numero1 == -1 and numero1 >= numero2:
        print("No hay un numero mayor")
    else:
        print("El numero mayor es:", numero2)


#Funcion para hacer una division
def dividirNumeros(dividendo, divisor):
    cantidad = dividendo
    contador = 0
    while cantidad >= divisor:
        cantidad = cantidad - divisor
        contador += 1
    print ("%d / %d = %d, sobra %d" %(dividendo, divisor, contador, cantidad))


#Funcion para mostrar el menu al usuario
def menu():
    print("Misión 07. Ciclos While")
    print("Autor: Joshua Sánchez Martínez")
    print("Matrícula: A01274269")
    print("1. Calcular divisores")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opción: "))
    return opcion


#Función principal
def main():
    opcion = menu()
    while opcion != 3:
        if opcion == 1:
            dividendo = int(input("Dividendo: "))
            divisor = int(input("Divisor: "))
            dividirNumeros(dividendo, divisor)
        elif opcion == 2:
            buscarNumeroMayor()
        elif opcion<1 or opcion>3:
            print("ERROR, teclea 1, 2 o 3.")

        opcion = menu()
    print("Fin del programa")


#Llamar a la funcion principal
main()