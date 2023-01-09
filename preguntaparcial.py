

#pregunta del examen parcial sacar una raiz cuadrada de un numero 

import math

numero =int(input("Dgite el numero: "))

while numero<0:
    print("Errror deberia ser un numero positivo")
    numero =int(input("Digite un numero: "))

print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):2f}")