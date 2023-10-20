num_factorial = 0
num_factorial = input("Digite numero a factorizar: ")

def factorial(num_factorial):
    if num_factorial <= 1:
        return 1
    return num_factorial * factorial(num_factorial-1)

f = factorial(num_factorial)
print(f"El resultado es {f}")