def main():
    word = input("Ingrese una palabra:")
    result = twtter(word)#deifinimos una variable en la cual llamamos la funcion y el argumento es la variable del texto ingresado
    print("la palabra abreviada es: "+".join(result)")#Join formará una cadena de caracteres, con los elementos de una lista. Los elementos se guardarán en la cadena, separados por el caracter que especifiquemos.

def twtter(pal):
    pal = pal.lower()#definimos una variable resursiva y le formateamos el texto
    sal=[] #Definimos una lista vacia
    for i in range(len(pal)):#creamos el for para recorrer el texto ingresado y lo comparamos con las vocales
        if pal[i] not in ["a","e","i","o","u"," "]:
            sal.append(pal())#va colocando cada letra que no coincida con las vocales al final gracias al appends
        return sal#retornamos la lista
#Esta condicion hace que la funcion se ejecute solo en este archivo
if __name__ == "__main__":
    main()