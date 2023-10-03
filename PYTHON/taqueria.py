#Menu de restaurante

#Definimos la funcion
def main():
#Definimos el diccionario
    menu = {
        "TACOS": 5.00,
        "BURRITO": 8.50,
        "BOWL": 9.50,
        "NACHOS": 11.00
    }
#Inicialzamos el contador en 0
    order_total = 0.0
    #pedimos que ingrese un articulo con un ciclo while
    while True:
        try:
            item = input("Ingrese articulo de su pedido: ")
        except EOFError:
            print("Error...")
            break
        #lo que digite el usuario todo lo manda con mayusculas, le decimos que si el articulo esta en el diccionario le sume el valor al total, si se quiere salir digita "CONTROL -D"
        #y si digita un articulo invalido muestra un error y no lo suma
        item = item.upper()
        if item in menu:
            order_total += menu[item]
        elif item == "CONTROL -D":
            print(f"Su totaL es: ${order_total:.2f}")
            break
        else:
            print("Articulo Invalido")
#Esta condicion hace que la funcion se ejecute solo en este archivos
if __name__ == "__main__":
    main()