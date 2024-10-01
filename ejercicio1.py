def promedio (lista):
    lista_numeros = input("Ingresa una lista de numeros: ")
    lista_numeros = [float(num) for num in lista_numeros.split(",")]
    return sum(lista_numeros) / len(lista_numeros)
print("El promedio de la lista es:", promedio([]))