
lista_nombres = ["Ines", "Paula", "Carlos", "Alberto", "Carol", "Maria", "Lucia"]
numero = int(input("Introduce un numero: "))

def ddg(lista_nombres, numero):
    if numero < len(lista_nombres):
        print(lista_nombres[numero])
        return

    else:
        print("Error.")

ddg(lista_nombres, numero)


