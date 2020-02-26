import os

def suma(x,y):
    return x+y
def resta(x,y):
    return x-y
def multiplica(x,y):
    return x*y
def divide(x,y):
    return x/y
def operar(func, x, y):
    return func(x, y)

while True:
    os.system("cls")
    print("\n\n\t+ Opciones:")
    print("\t+ Escriba 'suma' para sumar dos números")
    print("\t+ Escriba 'resta' para restar dos números")
    print("\t+ Escriba 'multiplica' para multiplicar dos números")
    print("\t+ Escriba 'divide' para dividir dos números")
    print("\t+ Escriba 'salir' para cerrar el programa")

    usr_input = input(">>:")

    if usr_input == "salir":
        break

    elif usr_input == "suma":
        try:
            num_1 = float(input("Ingrese un número: "))
            num_2 = float(input("Ingrese otro número: "))
            print(f"La suma es: {operar(suma, num_1, num_2)}")
        except ValueError:
            print("Entrada no válida")
        input("Presione Enter para continuar ")

    elif usr_input == "resta":
        try:
            num_1 = float(input("Ingrese un número: "))
            num_2 = float(input("Ingrese otro número: "))
            print(f"La resta es: {operar(resta, num_1, num_2)}")
        except ValueError:
            print("Entrada no válida")
        input("Presione Enter para continuar ")

    elif usr_input == "multiplica":
        try:
            num_1 = float(input("Ingrese un número: "))
            num_2 = float(input("Ingrese otro número: "))
            print(f"La multiplicación es: {operar(multiplica, num_1, num_2)}")
        except ValueError:
            print("Entrada no válida")
        input("Presione Enter para continuar ")

    elif usr_input == "divide":
        try:
            num_1 = float(input("Ingrese un número: "))
            num_2 = float(input("Ingrese otro número: "))
            print(f"La divición es: {operar(divide, num_1, num_2)}")
        except ValueError:
            print("Entrada no válida")
        except ZeroDivisionError:
            print("Entrada no válida")
        input("Presione Enter para continuar ")

    else:
        print("palabra incorrecta")
        input("Presione Enter para continuar ")
