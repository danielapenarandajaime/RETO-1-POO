# RETO-1-POO
## Reto 1 de POO, Daniela Peñaranda Jaime.
### 1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).
Asignamos el nombre "operaciones" a nuestra función, que  recibirá tres valores de entrada, dos enteros y un string y nos devolverá un entero. Luego, utilizando la estructura match-case le damos intrucciones a esta, para que, dependiendo del operador que ingrese el usuario, haga la operación correspondiente, y como ultima opción tenemos nuestro caso por defecto, en el que si no se cumplen ninguna de las condiciones anteriores nos va a decir que no ingresamos un operador valido.
```python
def operaciones(a: int,b: int,operacion: str) -> int:
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
Lo primero que hice fue crear la función palindromo, poniendo de parametro un string, y especificando que debe retornar otro string. El primer paso dentro de la función es convertir las mayúsculas que pueda tener la palabra a minusculas, para que al momento de compararlas no haya inconveniente; lo segundo es reemplazar las vocales con tilde a vocales sin tilde, para que al comparar sean iguales; definimos dos variables, "i" y "j", i será igual a la cantidad de letras de la palabra menos uno, pues en python la cuenta empieza desde 0 y termina en len(palabra)-1, y j será igual a 0, y definimos un bool que determinará si se cumple la condición de que sean iguales; se empieza un ciclo que va a comparar la primera letra con la ultima y así sucecivamente hasta terminar la palabra en el caso de que la cantidad de letras sea par, si es impar hasta que solo quede la letra del medio; si en cada iteración se cumplió la condición de que las letras sean iguales entonces nuestra palabra es un palíndromo, sino en algún momento de las iteraciones se rompe el ciclo y me arroja que no es un palíndromo. 
```python
def palindromo(palabra: str) -> str:
    palabramodificada = palabra.lower()
    palabramodificada = palabramodificada.replace('á', 'a') \
    .replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    i: int = len(palabramodificada) - 1
    j: int = 0
    palindromo: bool = False
    while i > len(palabra) / 2 and j < len(palabra) / 2:

        if palabramodificada[i] == palabramodificada[j]:
            palindromo = True
        else: 
            palindromo = False 

            break
        i -= 1
        j += 1
    if palindromo == True:
        return f"{palabra} es un palíndromo."
    else: return f"{palabra} no es un palíndromo."
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
Al crear la función definí el parametro de entrada (una lista de enteros) y el tipo de parametro de salida (una lista de enteros), luego de eso cree una lista de primos, que va a ser en la que se guardarán todos los primos que se encuentren en la lista de entrada. Hacemos un ciclo for, que tomará cada elemento de la lista, para evaluar si es primo o no, lo hará creando una variable boolean "esprimo", que será por defecto "True", lo que nos demostrará si es lo contrario es un while en el que dividiremos el numero por un j=2 que aumentará 1 con cada iteración mientras que j * j sea menor o igual a el numero, de esta forma si se encuentran divisores nos romperá el ciclo y obtendremos que el numero no es primo, de lo contrario sabremos que el número es primo y se guardará en la lista de primos que se retornará al final de la función.
```python
def determinarprimos(lista: list[int]) -> list[int]:
    primos: list[int] = []
    for numero in lista:
        esprimo: bool = True
        j: int = 2
        divisores: list[int] = []
        while j * j <= numero:
            if numero % j == 0:
                esprimo = False
                break
            j += 1

        if esprimo == True and numero >= 2:
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
Definimos la función que tonará como valor de entrada una lista de enteros y nos retornará un entero, se crean dos variables igual a 0, y una i = 0 que aumentará con cada iteración mientras sea menor a la cantidad de elementos de la lista menos uno, con cada iteración se sumará el número ubicado en la posición i y el número siguiente a ese, se comparará con la variable de sumamayor, y si es mayor a esta, sumamayor tomará su valor, sino sumamayor seguirá con el valor de antes, de esta forma, cuando encuentre la suma mayor, esta quedará almacenada en esa variable y ninguna de las otras sumas la podrá reemplazar, al final la función nos retornará el valor de la suma mayor.
```python
def mayorsuma(lista: list[int]) -> int:
    sumauno = 0
    sumamayor = 0
    i = 0
    while i < len(lista) - 1:
        sumauno = lista[i] + lista[i + 1]

        if sumauno >= sumamayor:
            sumamayor = sumauno
            
        i += 1

    return sumamayor
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
### 5. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.
