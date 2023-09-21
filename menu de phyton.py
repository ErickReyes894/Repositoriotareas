Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def binario_a_decimal(binario):
    decimal = 0
    for i in range(len(binario)):
        decimal += int(binario[i]) * 2**(len(binario) - i - 1)
    return decimal

def decimal_a_binario(decimal):
    return bin(decimal).replace("0b", "")

while True:
    print("Operaciones disponibles:")
    print("1. Convertir de binario a decimal")
    print("2. Convertir de decimal a binario")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sumar")
    print("6. Restar")
    print("7. Salir")
    
...     opcion = input("Selecciona una operación (1/2/3/4/5/6/7): ")
...     
...     if opcion == "1":
...         binario = input("Introduce un número binario: ")
...         decimal = binario_a_decimal(binario)
...         print("El número decimal equivalente es:", decimal)
...     elif opcion == "2":
...         decimal = int(input("Introduce un número decimal: "))
...         binario = decimal_a_binario(decimal)
...         print("El número binario equivalente es:", binario)
...     elif opcion == "3":
...         num1 = float(input("Introduce el primer número: "))
...         num2 = float(input("Introduce el segundo número: "))
...         resultado = num1 * num2
...         print("El resultado de la multiplicación es:", resultado)
...     elif opcion == "4":
...         num1 = float(input("Introduce el dividendo: "))
...         num2 = float(input("Introduce el divisor: "))
...         if num2 != 0:
...             resultado = num1 / num2
...             print("El resultado de la división es:", resultado)
...         else:
...             print("No se puede dividir por cero.")
...     elif opcion == "5":
...         num1 = float(input("Introduce el primer número: "))
...         num2 = float(input("Introduce el segundo número: "))
...         resultado = num1 + num2
...         print("El resultado de la suma es:", resultado)
...     elif opcion == "6":
...         num1 = float(input("Introduce el minuendo: "))
...         num2 = float(input("Introduce el sustraendo: "))
...         resultado = num1 - num2
...         print("El resultado de la resta es:", resultado)
...     elif opcion == "7":
...         print("¡Hasta luego!")
...         break
...     else:
...         print("Opción no válida. Por favor, selecciona una opción válida (1/2/3/4/5/6/7).")
