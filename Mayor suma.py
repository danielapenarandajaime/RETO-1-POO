def mayor_suma(lista: list[int]) -> int:

    # Definimos las variables
    suma_uno = 0
    suma_mayor = 0
    i = 0

    # Creamos un ciclo que nos haga cada suma y las compare
    while i < len(lista) - 1:
        suma_uno = lista[i] + lista[i + 1]

        # Comparamos la suma realizada con la suma mayor
        if suma_uno >= suma_mayor:
            # si la suma resulta ser mayor se guardará en la variable suma_mayor
            suma_mayor = suma_uno
            
        i += 1

    return suma_mayor

# Casos de prueba
print(mayor_suma([11, 21, 34, 46, 58, 60, 71, 81, 91, 101]))
print(mayor_suma([30, 45, 67, 234, 31, 24]))


                


    

