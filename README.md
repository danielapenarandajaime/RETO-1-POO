# RETO-1-POO
## Reto 1 de la Clase 4 del curso de Programación Orientada a Objetos del profesor Felipe Gonzales Roldán
### 1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).
Asignamos el nombre "operaciones" a nuestra función, y utilizando la estructura match-case le damos intrucciones a la función, para que dependiendo del operador que ingrese el usuario haga la operación correspondiente, y como ultima opción tenemos nuestro caso por defecto, en el que si no se cumplen ninguna de las condiciones anteriores nos va a decir que no ingresamos el operador correcto.
```python
def operaciones(a: int,b: int,operacion: str):
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
