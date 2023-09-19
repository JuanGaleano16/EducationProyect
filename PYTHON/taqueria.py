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
#Recorremos
while True:
    try:
        item = input("Ingrese artifculo de su pedido: ")
    except EOFError:
        print("Error...")
        break
    item = item.upper()
    if item in menu:
        order_total += menu[item]
    elif item == "CONTROL -D":
        print("Su totaL es: ${order_total:.2f}")
        break
    else:
        print("Articulo Invalido")

if __name__ == "__main__":
    main()