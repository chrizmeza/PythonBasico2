print("========Calculadora==========")

num_1 = float(input("Escribe tu valor del primer numero: "))
num_2 = float(input("Escribe tu valor del segundo numero: "))
operacion = input(" Que operacion quieres usar +, -, *, / -> ")


def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def multiplicacion(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 == 0:
        return "Error (no se puede dividir por cero)"
    return n1 / n2


if operacion == "+":
    resultado = suma(num_1, num_2)
    print("El resultado de la suma es: ", resultado)

if operacion == "-":
    resultado = resta(num_1, num_2)
    print("El resultado de la resta es: ", resultado)

if operacion == "*":
    resultado = multiplicacion(num_1, num_2)
    print("El resultado de la multiplicación es: ", resultado)

if operacion == "/":
    resultado = division(num_1, num_2)
    print("El resultado de la división es: ", resultado)