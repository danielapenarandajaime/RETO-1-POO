def determinarprimos(lista: list[int]) -> list[int]:
    primos: list[int] = []

    for numero in lista:
        es_primo: bool = True
        j: int = 2

        while j * j <= numero:
            # Si el número tiene un divisor además de el mismo no es primo
            if numero % j == 0:
                es_primo = False
                break
            j += 1

        if es_primo == True and numero >= 2:
            primos.append(numero)

    return primos

print(determinarprimos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(determinarprimos([11, 21, 34, 46, 58, 60, 71, 81, 91, 101]))