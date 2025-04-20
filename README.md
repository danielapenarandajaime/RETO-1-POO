# RETO-1-POO
## Reto 1 de POO, Daniela Peñaranda Jaime.
### 1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

La función recibirá tres valores de entrada, dos enteros y un string y nos devolverá un entero. Luego, utilizando la estructura match-case le damos intrucciones a esta, para que, dependiendo del operador que ingrese el usuario, haga la operación correspondiente, y como ultima opción tenemos nuestro caso por defecto, en el que si no se cumplen ninguna de las condiciones anteriores nos va a decir que no ingresamos un operador valido.
```python
def operaciones(a: int,b: int,operacion: str) -> int:
    
    # Revisa el caracter ingresado y realiza la operación correspondiente
    match operacion:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*" | "x":
            return a * b
        case "/" | "÷":
            if b == 0:
                return "No se puede dividir por 0."
            else: return a / b
        case _:
            return "No ingresaste un operador valido"
```
*Casos de prueba:*
```python
print(operaciones(4, 3, "+"))
print(operaciones(4, 4, "-"))
print(operaciones(5, 2, "*"))
print(operaciones(8, 2, "x"))
print(operaciones(10, 0, "/"))
print(operaciones(12, 2, "÷"))
print(operaciones(4, 2, "´"))
```
*Resultado por terminal:*
```
7
0
10
16
No se puede dividir por 0.
6.0
No ingresaste un operador valido
```

### 2. Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

El primer paso dentro de la función es convertir las mayúsculas que pueda tener la palabra a minusculas, para que al momento de compararlas no haya inconveniente; lo segundo es reemplazar las vocales con tilde a vocales sin tilde, para que al comparar sean iguales; definimos dos variables, "i" y "j", i será igual a la cantidad de letras de la palabra menos uno, pues en python la cuenta empieza desde 0 y termina en len(palabra)-1, y j será igual a 0, y definimos un bool que determinará si se cumple la condición de que sean iguales; se empieza un ciclo que va a comparar la primera letra con la ultima y así sucecivamente hasta terminar la palabra en el caso de que la cantidad de letras sea par, si es impar hasta que solo quede la letra del medio; si en cada iteración se cumplió la condición de que las letras sean iguales entonces nuestra palabra es un palíndromo, sino en algún momento de las iteraciones se rompe el ciclo y me arroja que no es un palíndromo. 
```python
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
```
*Casos de prueba:*
```python
print(palindromo("ÁÉÍÓÚÓÍÉÁ"))
print(palindromo("AEIOOIEÁ"))
print(palindromo("rana"))
```
*Resultado por terminal:*
```
ÁÉÍÓÚÓÍÉÁ es un palíndromo.
AEIOOIEÁ es un palíndromo.
rana no es un palíndromo.
```
### 3. Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

Se crea una lista de primos, que va a ser en la que se guardarán todos los primos que se encuentren en la lista de entrada. Hacemos un ciclo for, que tomará cada elemento de la lista, para evaluar si es primo o no, lo hará creando una variable boolean "esprimo", que será por defecto "True", lo que nos demostrará si es lo contrario es un while en el que dividiremos el numero por un j=2 que aumentará 1 con cada iteración mientras que j * j sea menor o igual a el numero, de esta forma si se encuentran divisores nos romperá el ciclo y obtendremos que el numero no es primo, de lo contrario sabremos que el número es primo y se guardará en la lista de primos que se retornará al final de la función.
```python
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

```
*Casos de prueba:*
```python
print(determinarprimos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(determinarprimos([11, 21, 34, 46, 58, 60, 71, 81, 91, 101]))
```
*Resultado por terminal:*
```
[2, 3, 5, 7]
[11, 71, 101]
```
### 4. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

Se crean dos variables igual a 0, y una i = 0 que aumentará con cada iteración mientras sea menor a la cantidad de elementos de la lista menos uno, con cada iteración se sumará el número ubicado en la posición i y el número siguiente a ese, se comparará con la variable de sumamayor, y si es mayor a esta, sumamayor tomará su valor, sino sumamayor seguirá con el valor de antes, de esta forma, cuando encuentre la suma mayor, esta quedará almacenada en esa variable y ninguna de las otras sumas la podrá reemplazar, al final la función nos retornará el valor de la suma mayor.
```python
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
```
*Casos de prueba:*
```python
print(mayorsuma([11, 21, 34, 46, 58, 60, 71, 81, 91, 101]))
print(mayorsuma([30, 45, 67, 234, 31, 24]))
```
*Resultado por terminal:*
```
192
301
```
### 5. Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]
Se crean dos funciones, la primera "conversion_ascii", que tomará cada palabra de la lista inicial, le quitará mayusculas y tildes, y luego de eso toma cada letra de cada palabra y la transforma a codigo ascii, almacenandola en una lista unica de cada palabra, esta lista uego será ordenada internamente con "sorted" de menor a mayor número interno, y por ultimo se almacena en una lista adicional, que se retorna.
```python
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
```
En la segunda función (la principal), se llama a la función  "conversion_ascii", para que defina a la variable de lista_dos, y con un ciclo se compara al elemento lista_dos[i] con todos los elementos siguientes a el, si las dos listas tienen el mismo tamaño se entra a comparar cada elemento de las listas, si son iguales se agregara el elemento i y j de la lista original a la lista de resultado, sino se rompe el ciclo y se sigue con el siguiente. Cuando se tiene la lista final, a través de list(dict.fromkeys() se buscan elementos repetidos y se eliminan de la lista.
```python
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
```
*Casos de prueba:*
```python
print(comparar(["amor", "ramo", "perro"]))
print(comparar(["rrope", "amo", "perro", "errop"]))
```
*Resultado por terminal:*
```
['amor', 'ramo']
['rrope', 'perro', 'errop']
```

