# PRACTICA 5 - OCP - Calculadora que cumple el principio Abierto/Cerrado

# Cada comportamiento en su propia función
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

# Diccionario que permite extender sin modificar
operaciones = {
    "suma": sumar,
    "resta": restar,
    "multiplicacion": multiplicar,
    "division": dividir
}

def calculadora_ocp(a, b, operacion):
    if operacion in operaciones:
        return operaciones[operacion](a, b)
    else:
        return "Operación no válida"

# --- PRUEBA DEL PASO 3 ---
print("Prueba base:")
print("5 + 3 =", calculadora_ocp(5, 3, "suma"))
print("5 - 3 =", calculadora_ocp(5, 3, "resta"))

# --- PRUEBA DEL PASO 4: AGREGAR OPCIÓN NUEVA SIN TOCAR LO ANTERIOR ---
def potencia(a, b):
    return a ** b

operaciones["potencia"] = potencia

print("\nPrueba de extensión (sin modificar código viejo):")
print("2 elevado a 3 =", calculadora_ocp(2, 3, "potencia"))