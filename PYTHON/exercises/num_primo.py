"""Leer el número desde el usuario.
Inicializar una variable booleana es_primo como verdadera.
Verificar si el número es menor o igual a 1. En ese caso, asignares_primo como falso.
Iterar desde 2 hasta la mitad del número (redondeando hacia arriba).
Si el número es divisible entre cualquier valor en ese rango, asignares_primo como falso y salir del bucle.
Si es_primo es verdadera, imprimir "El número es primo".
De lo contrario, imprimir "El número no es primo"."""

num = int(input("Digite un numero entero positivo: "))

es_primo = True

if num <= 1:
    es_primo = False
"""else:
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            es_primo = False
            break"""

if es_primo:
    print("EL NUMERO ES PRIMO")
else:
    print("El NUMERO NO ES PRIMO")