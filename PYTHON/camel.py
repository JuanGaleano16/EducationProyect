camel_case = input("Ingrese nomre de variable en camelCase: ")
snake_case = ""

for i in range(len(camel_case)):
    if camel_case[i].isupper():
        snake_case += "_" + camel_case[i].lower()
    else:
        snake_case += camel_case[i]

print("El nombre de la variable snake case es: ", snake_case)