# Convierte los elementos de la lista en código ascii
def conversion_ascii(lista: list[str]) -> list[str]:
    lista_dos: list[int] = []

    for palabra in lista:
        # Quitamos las tildes y las mayusculas de cada palabra
        palabra_modificada = palabra.lower()
        palabra_modificada = palabra.replace('á', 'a') \
    .replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
        palabra_mod = []

        # Cada letra la convertimos a ascii y la almacenamos en otra lista
        for letra in palabra_modificada:
            palabra_mod.append(ord(letra))

        # Ordenamos la lista de menor a mayor numero
        palabra_mod = sorted(palabra_mod)
        # Agregamos la lista a la lista dos
        lista_dos.append(palabra_mod)

    return lista_dos

# Compara cada lista y verifica si son iguales
def comparar(lista: list[str]) -> list[str]:
    # Creamos la lista a retornar y la lista dos
    resultado: list[int] = []
    lista_dos: list[int] = conversion_ascii(lista)
    i = 0

    # Comparamos cada lista con las listas siguientes a ella
    while i < len(lista_dos) - 1:
        j = i + 1

        # J aumentará para comparar al elemento con los elementos siguientes a el
        while j < len(lista_dos):

            # Si tienen la misma cantidad de lementos se compararán
            if len(lista_dos[i]) == len(lista_dos[j]):
                elemento = lista_dos[j]
                k = 0
                iguales: bool = True

                # Se compara cada elemento de las listas
                for element in lista_dos[i]:

                    # Si no son iguales se rompe el ciclo
                    if elemento[k] != element:
                        iguales = False
                        break
                    k +=1

                # Si son iguales se guardan los elementos de la lista original
                if iguales == True:
                    resultado.append(lista[i])
                    resultado.append(lista[j])
        
            j += 1
        # Se repite el ciclo
        i += 1
    # Se revisa la lista, si hay elementos repetidos se eliminan
    resultado = list(dict.fromkeys(resultado))
   
    return resultado

print(comparar(["amor", "ramo", "perro"]))
print(comparar(["rrope", "amo", "perro", "errop"]))