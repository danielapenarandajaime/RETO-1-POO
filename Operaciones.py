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

print(operaciones(4, 3, "+"))
print(operaciones(4, 4, "-"))
print(operaciones(5, 2, "*"))
print(operaciones(8, 2, "x"))
print(operaciones(10, 0, "/"))
print(operaciones(12, 2, "÷"))
print(operaciones(4, 2, "´"))