# ============================================================
#  Hoja de Trabajo — Introducción a Python  (SOLUCIONES)
# ============================================================

# ==============================================================
# 1. Hola Mundo y print()
# ==============================================================

# Ejercicio 1a
# Imprime nombre y carnet en una sola línea usando dos argumentos.
print("Nombre: Ana", "Carnet: 202300001")

# Ejercicio 1b
# Usa end="" para imprimir en una sola línea con varias llamadas.
print("Hola ", end="")
print("desde ", end="")
print("Python")


# ==============================================================
# 2. Variables y tipos de datos
# ==============================================================

# Ejercicio 2a
nombre   = "Ana García"
edad     = 20
promedio = 85.5
activo   = True

print(f"nombre:   {nombre}   ({type(nombre).__name__})")
print(f"edad:     {edad}     ({type(edad).__name__})")
print(f"promedio: {promedio} ({type(promedio).__name__})")
print(f"activo:   {activo}   ({type(activo).__name__})")

# Ejercicio 2b
# Asignación múltiple en una sola línea.
x, y, z = 10, 20, 30
print(f"x={x}, y={y}, z={z}")


# ==============================================================
# 3. Operaciones aritméticas
# ==============================================================

# Ejercicio 3a
a, b = 23, 7
print(f"División entera:  {a // b}")
print(f"Residuo (módulo): {a % b}")
print(f"a elevado a b:    {a ** b}")

# Ejercicio 3b
import math

print(f"Raíz cuadrada de 144:       {math.sqrt(144)}")
print(f"Techo de 7.3:               {math.ceil(7.3)}")
print(f"Piso de 7.9:                {math.floor(7.9)}")
print(f"Pi redondeado a 4 decimales:{math.pi:.4f}")


# ==============================================================
# 4. Strings y métodos útiles
# ==============================================================

# Ejercicio 4a
cadena = "  fisica y matematica  "
sin_espacios  = cadena.strip()
print(sin_espacios)
en_mayusculas = sin_espacios.upper()
print(en_mayusculas)
reemplazado   = en_mayusculas.replace("Y", "&")
print(reemplazado)

# Ejercicio 4b
colores_str = "rojo-verde-azul-amarillo"
colores = colores_str.split("-")
print(colores)
unidos = " | ".join(colores)
print(unidos)
print("verde" in colores)


# ==============================================================
# 5. Listas
# ==============================================================

# Ejercicio 5a
materias = ["Cálculo", "Física", "Programación", "Álgebra"]
materias.append("Estadística")       # 1. Agrega al final
materias.insert(2, "Química")        # 2. Inserta en posición 2
materias.remove("Álgebra")           # 3. Elimina "Álgebra"
print(materias)
print(f"Longitud: {len(materias)}")

# Ejercicio 5b
notas = [78, 92, 65, 88, 74, 95, 61, 83]
print(f"Mínimo:   {min(notas)}")
print(f"Máximo:   {max(notas)}")
print(f"Suma:     {sum(notas)}")
print(f"Promedio: {sum(notas) / len(notas):.2f}")


# ==============================================================
# 6. Diccionarios
# ==============================================================

# Ejercicio 6a
curso = {
    "nombre":   "Introducción a Python",
    "codigo":   "CC101",
    "creditos": 4,
    "activo":   True
}
curso["estudiantes"] = 35                               # 1. Nueva clave
print(curso.get("creditos"))                            # 2. Acceso seguro
print(curso.get("salon", "Sin asignar"))                # 3. Clave inexistente

# Ejercicio 6b
for clave, valor in curso.items():
    print(f"{clave:12} : {valor}")


# ==============================================================
# 7. Condicionales
# ==============================================================

# Ejercicio 7a
def clasificar_imc(imc):
    """Clasifica el Índice de Masa Corporal."""
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

for valor in [16.0, 22.5, 27.3, 31.8]:
    print(f"IMC {valor}: {clasificar_imc(valor)}")

# Ejercicio 7b — Operador ternario
for num in [4, 7, 0]:
    resultado = "par" if num % 2 == 0 else "impar"
    print(f"{num} es {resultado}")


# ==============================================================
# 8. Ciclos
# ==============================================================

# Ejercicio 8a — for con enumerate()
planetas = ["Mercurio", "Venus", "Tierra", "Marte",
            "Júpiter", "Saturno", "Urano", "Neptuno"]
for i, planeta in enumerate(planetas, start=1):
    print(f"[{i}] {planeta}")

# Ejercicio 8b — while: tabla del 7
i = 1
while i <= 10:
    print(f"7 x {i} = {7 * i}")
    i += 1

# Ejercicio 8c — List comprehension
cubos     = [x**3 for x in range(1, 9)]
div3_no9  = [x for x in range(1, 31) if x % 3 == 0 and x % 9 != 0]
print(cubos)
print(div3_no9)


# ==============================================================
# 9. Funciones
# ==============================================================

# Ejercicio 9a
def convertir_temperatura(grados, escala="C"):
    """Convierte entre Celsius y Fahrenheit."""
    if escala == "C":
        return grados * 9 / 5 + 32
    elif escala == "F":
        return (grados - 32) * 5 / 9

print(convertir_temperatura(100))        # 100 °C → F
print(convertir_temperatura(0))          #   0 °C → F
print(convertir_temperatura(32,  "F"))   #  32 °F → C
print(convertir_temperatura(212, "F"))   # 212 °F → C

# Ejercicio 9b
def resumen_lista(lista):
    """Retorna (mínimo, máximo, promedio) de una lista."""
    return min(lista), max(lista), sum(lista) / len(lista)

minimo, maximo, prom = resumen_lista([12, 45, 7, 89, 34, 56, 23])
print(f"Mínimo: {minimo}  Máximo: {maximo}  Promedio: {prom:.2f}")

# Ejercicio 9c — Recursión: Fibonacci
def fibonacci(n):
    """Retorna el n-ésimo número de Fibonacci."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(f"fibonacci({i}) = {fibonacci(i)}")


# ==============================================================
# 10. Manejo de errores
# ==============================================================

# Ejercicio 10a
def convertir_entero(valor):
    """Intenta convertir valor a entero con manejo de errores."""
    try:
        resultado = int(valor)
        return resultado
    except ValueError:
        print(f"Error: '{valor}' no se puede convertir a entero.")
        return None
    finally:
        print(f"[intento con: {valor}]")

for v in ["42", "3.14", "hola", 100]:
    convertir_entero(v)

# Ejercicio 10b
def validar_edad(edad):
    """Valida que la edad sea un entero entre 0 y 150."""
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un entero.")
    if edad < 0 or edad > 150:
        raise ValueError("La edad debe estar entre 0 y 150.")
    return True

for valor in [25, -5, 200, "veinte"]:
    try:
        print(validar_edad(valor))
    except (TypeError, ValueError) as e:
        print(f"Error con {valor!r}: {e}")


# ==============================================================
# Ejercicio Integrador
# ==============================================================

def analizar_curso(estudiantes):
    """
    Recibe una lista de dicts con 'nombre' y 'notas'.
    Imprime tabla de resultados y conteo de aprobados/reprobados.
    """
    aprobados  = 0
    reprobados = 0

    print(f"\n{'Nombre':<15} {'Promedio':>10} {'Estado':>12}")
    print("-" * 40)

    for est in estudiantes:
        nombre = est["nombre"]
        notas  = est["notas"]

        if not notas:
            promedio = None
            estado   = "Sin notas"
        else:
            promedio = sum(notas) / len(notas)
            if promedio >= 61:
                estado = "Aprobado"
                aprobados += 1
            else:
                estado = "Reprobado"
                reprobados += 1

        prom_str = f"{promedio:.2f}" if promedio is not None else "N/A"
        print(f"{nombre:<15} {prom_str:>10} {estado:>12}")

    print("-" * 40)
    print(f"Aprobados: {aprobados}  |  Reprobados: {reprobados}\n")


curso = [
    {"nombre": "Ana López",   "notas": [85, 90, 78, 92]},
    {"nombre": "Carlos Ruiz", "notas": [55, 48, 60, 52]},
    {"nombre": "María Paz",   "notas": [70, 75, 68, 80]},
    {"nombre": "Luis Gómez",  "notas": [95, 98, 100, 92]},
    {"nombre": "Sara Díaz",   "notas": [40, 55, 50, 45]},
    {"nombre": "Pedro Alva",  "notas": []},
]

analizar_curso(curso)
