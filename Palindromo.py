def palindromo(palabra: str) -> str:
    # Quitamos mayusculas y tildes
    palabra_modificada = palabra.lower()
    palabra_modificada = palabra_modificada.replace('á', 'a') \
    .replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    i: int = len(palabra_modificada) - 1
    j: int = 0
    palindromo: bool = False

    while i > len(palabra) / 2 and j < len(palabra) / 2:

        """ Comparamos elementos en la posición opuesta
            Ejemplo: 
            palabra = erisire
            Se compara el primero con el ultimo: "e" con "e"
            el penultimo con el segundo: "r" con "r"
            y así sucesivamente
        """
        if palabra_modificada[i] == palabra_modificada[j]:
            palindromo = True
        else: 
            break
        i -= 1
        j += 1

    if palindromo == True:
        return f"{palabra} es un palíndromo."
    else: return f"{palabra} no es un palíndromo."

print(palindromo("ÁÉÍÓÚÓÍÉÁ"))
print(palindromo("AEIOOIEÁ"))
print(palindromo("rana"))