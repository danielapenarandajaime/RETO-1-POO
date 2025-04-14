# RETO-1-POO
## Reto 1 de POO, Daniela Peñaranda Jaime.
### 1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).
Asignamos el nombre "operaciones" a nuestra función, y utilizando la estructura match-case le damos intrucciones a esta, para que, dependiendo del operador que ingrese el usuario, haga la operación correspondiente, y como ultima opción tenemos nuestro caso por defecto, en el que si no se cumplen ninguna de las condiciones anteriores nos va a decir que no ingresamos un operador valido.
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
print(operaciones(4,3,"+"))
print(operaciones(4,4,"-"))
print(operaciones(5,2,"*"))
print(operaciones(8,2,"x"))
print(operaciones(10,0,"/"))
print(operaciones(12,2,"÷"))
print(operaciones(4,2,"´"))
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
    .replace('é', 'e').replace('í','i').replace('ó','o').replace('ú','u')
    i: int = len(palabramodificada)-1
    j: int = 0
    palindromo: bool = False
    while i>len(palabra)/2 and j<len(palabra)/2:

        if palabramodificada[i]==palabramodificada[j]:
            palindromo = True
        else: 
            palindromo = False 

            break
        i-=1
        j+=1
    if palindromo == True:
        return f"{palabra} es un palíndromo."
    else: return f"{palabra} no es un palíndromo."
```
*Casos de prueba: *
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
