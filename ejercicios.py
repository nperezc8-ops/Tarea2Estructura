# =====================================================================
#  ejercicios.py  —  OPCIÓN 3 DEL MENÚ: "Listar ejercicios"
# ---------------------------------------------------------------------
#  Aquí van TODOS los ejercicios del módulo 📋 Listas de la guía:
#     • 3 ejercicios DESARROLLADOS (taller paso a paso)  -> T1, T2, T3
#     • 5 ejercicios PROPUESTOS (solución oculta)         -> P1 ... P5
#
#  Cada ejercicio es UNA función sin parámetros que:
#     1) imprime su enunciado corto,
#     2) usa datos fijos de prueba (los indicados en cada función),
#     3) muestra el resultado.
#
#  REGLA: en cada ejercicio resuelve con DOS versiones cuando se indique:
#     ✋ MANUAL (bucles, patrones del módulo 0)  y  🐍 PYTHON (built-ins
#     y comprensiones). Imprime ambas para comparar.

# =====================================================================


# ============================ DESARROLLADOS ==========================

def ejercicio_t1():
    """
    T1 — CRUD de pasajeros con clase Pasajero + list   (Taller, Medio)
    -----------------------------------------------------------------
    Demuestra (sin menú, con llamadas directas) el CRUD completo usando
    tu clase ListaPasajerosPython:
        añadir 3 pasajeros -> listar -> buscar por cédula -> modificar
        -> eliminar -> listar otra vez -> ordenar por NOMBRE con
        sort(key=lambda p: p.nombre)  (es el reto del taller).
    Importa así:  from lista_python import ListaPasajerosPython
                  from pasajero import Pasajero
    """
    from lista_python import ListaPasajerosPython
    from pasajero import Pasajero

    print("T1 — CRUD de pasajeros con clase Pasajero + list")
    lista = ListaPasajerosPython()
    lista.añadir(Pasajero("Diana", "0923456789", 22))
    lista.añadir(Pasajero("Ana", "0912345678", 28))
    lista.añadir(Pasajero("Luis", "0987654321", 35))
    print("Añadir tres pasajeros:")
    lista.listar()

    pos = lista.buscar("0987654321")
    print(f"Buscar a Luis: posición {pos}")
    if pos != -1:
        print(lista.pasajeros[pos])

    if lista.modificar("0987654321", "Luis Alberto", 36):
        print("Pasajero modificado:")
        lista.listar()

    if lista.eliminar_por_valor("0912345678"):
        print("Eliminar a Ana:")
        lista.listar()

    lista.pasajeros.sort(key=lambda p: p.nombre)
    print("Ordenar por nombre:")
    lista.listar()


def ejercicio_t2():
    """
    T2 — Estadísticas de una lista de notas   (Taller, Medio)
    -----------------------------------------------------------------
    Datos:  nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
            notas   = [ 8,     6,      10,      7,      5  ]
    Muestra: promedio, máxima, mínima, cantidad de aprobados (>= 7)
             y el nombre del mejor estudiante.
    ✋ MANUAL : un solo for con acumulador, campeón y contador.
    🐍 PYTHON : sum, max, min, len, notas.index(max(notas)) y
               aprobados con COMPRENSIÓN: [n for n in notas if n >= 7]
    Salida esperada: Promedio 7.20 · Máx 10 (Diana) · Mín 5 · Aprobados 3 de 5
    """
    print("T2 — Estadísticas de una lista de notas")
    nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
    notas = [8, 6, 10, 7, 5]


    total = 0
    maxima = notas[0]
    minima = notas[0]
    mejor = nombres[0]
    aprobados = 0
    for i in range(len(notas)):
        total = total + notas[i]
        if notas[i] > maxima:
            maxima = notas[i]
            mejor = nombres[i]
        if notas[i] < minima:
            minima = notas[i]
        if notas[i] >= 7:
            aprobados = aprobados + 1
    promedio = total / len(notas)
    print(f"Manual: Promedio {promedio:.2f} · Máx {maxima} ({mejor}) · "
          f"Mín {minima} · Aprobados {aprobados} de {len(notas)}")


    promedio = sum(notas) / len(notas)
    maxima = max(notas)
    minima = min(notas)
    mejor = nombres[notas.index(max(notas))]
    aprobados = [n for n in notas if n >= 7]
    print(f"Python: Promedio {promedio:.2f} · Máx {maxima} ({mejor}) · "
          f"Mín {minima} · Aprobados {len(aprobados)} de {len(notas)}")


def ejercicio_t3():
    """
    T3 — Ordenar una lista (bubble sort)   (Taller, Avanzado)
    -----------------------------------------------------------------
    Datos: [5, 2, 8, 1, 9, 3, 7]
    ✋ MANUAL : burbuja con bandera hubo_swap (sobre una COPIA lista[:]).
    🐍 PYTHON : sorted(lista) y lista.sort(reverse=True).
    Extra    : palabras = ["python", "a", "código", "el"] ordenadas con key=len
    Salida esperada: [1, 2, 3, 5, 7, 8, 9]
    """
    print("T3 — Ordenar una lista (bubble sort)")
    lista = [5, 2, 8, 1, 9, 3, 7]
    copia = lista[:]

    for vuelta in range(len(copia) - 1):
        hubo_swap = False
        for i in range(len(copia) - 1 - vuelta):
            if copia[i] > copia[i + 1]:
                aux = copia[i]
                copia[i] = copia[i + 1]
                copia[i + 1] = aux
                hubo_swap = True
        if not hubo_swap:
            break
    print("Manual: Burbuja:", copia)
    print("Lista original:", lista)

    print("Python: sorted:", sorted(lista))
    descendente = lista.copy()
    descendente.sort(reverse=True)
    print("Python: sort descendente:", descendente)

    palabras = ["python", "a", "código", "el"]
    print("Palabras por longitud:", sorted(palabras, key=len))


# ============================= PROPUESTOS ============================

def ejercicio_p1():
    """
    P1 — Contar apariciones de un valor
    Datos: lista = [1, 3, 2, 3, 4, 3, 5],  v = 3
    ✋ MANUAL : patrón contador.   🐍 PYTHON : lista.count(v)
    🧩 COMPRENSIÓN: len([x for x in lista if x == v])
    Salida esperada: 3 aparece 3 veces
    """
    print("P1 — Contar apariciones de un valor")
    lista = [1, 3, 2, 3, 4, 3, 5]
    v = 3

    cantidad = 0
    for x in lista:
        if x == v:
            cantidad = cantidad + 1
    print(f"Manual: {v} aparece {cantidad} veces")
    print(f"Python: count: {v} aparece {lista.count(v)} veces")
    coincidencias = [x for x in lista if x == v]
    print(f"Comprensión: {v} aparece {len(coincidencias)} veces")


def ejercicio_p2():
    """
    P2 — Invertir una lista SIN lista.reverse()
    Datos: [1, 2, 3, 4, 5]
    ✋ MANUAL : for con range(len(lista)-1, -1, -1) y append.
    🐍 PYTHON : lista[::-1]  y  list(reversed(lista))
    🧩 COMPRENSIÓN: [lista[i] for i in range(len(lista)-1, -1, -1)]
    Salida esperada: [5, 4, 3, 2, 1]
    """
    print("P2 — Invertir una lista sin reverse()")
    lista = [1, 2, 3, 4, 5]

    invertida = []
    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])
    print("Manual: Recorrido hacia atrás:", invertida)
    print("Python: Slicing:", lista[::-1])
    print("Python: reversed:", list(reversed(lista)))
    invertida_comprension = [lista[i] for i in range(len(lista) - 1, -1, -1)]
    print("Comprensión:", invertida_comprension)


def ejercicio_p3():
    """
    P3 — Números únicos manteniendo el orden
    Datos: [1, 3, 2, 3, 4, 1, 5, 2]
    ✋ MANUAL : recorrer y añadir si "not in unicos".
    🐍 PYTHON : list(dict.fromkeys(nums))   (y explica por qué list(set(nums))
               NO garantiza el orden)
    Salida esperada: [1, 3, 2, 4, 5]
    """
    print("P3 — Números únicos manteniendo el orden")
    nums = [1, 3, 2, 3, 4, 1, 5, 2]

    unicos = []
    for numero in nums:
        if numero not in unicos:
            unicos.append(numero)
    print("Manual: Recorrido manual:", unicos)
    print("Python: dict.fromkeys:", list(dict.fromkeys(nums)))


    print("dict conserva el orden de aparición; set no garantiza ese orden.")


def ejercicio_p4():
    """
    P4 — Segundo mayor (sin ordenar toda la lista)
    Datos: [5, 2, 9, 7, 9, 3, 8]
    ✋ MANUAL : dos campeones (mayor y segundo) en un solo recorrido.
    🐍 PYTHON (para comprobar): sorted(set(nums))[-2]
    Salida esperada: Mayor 9 · Segundo 8
    """
    print("P4 — Segundo mayor sin ordenar toda la lista")
    nums = [5, 2, 9, 7, 9, 3, 8]
    mayor = nums[0]
    segundo = None

    for numero in nums:
        if numero > mayor:
            segundo = mayor
            mayor = numero
        elif numero != mayor:
            if segundo is None or numero > segundo:
                segundo = numero
    print(f"Manual: Mayor {mayor} · Segundo {segundo}")

    comprobacion = sorted(set(nums))
    print(f"Python: Mayor {comprobacion[-1]} · Segundo {comprobacion[-2]}")


def ejercicio_p5():
    """
    P5 — Fusionar dos listas ordenadas (sin sort)
    Datos: a = [1, 3, 5, 7],  b = [2, 4, 6, 8, 10]
    ✋ MANUAL : dos índices i, j comparando cabezas (base del merge sort)
               y al final extend con lo que sobre.
    🐍 PYTHON (para comprobar): sorted(a + b)
    Salida esperada: [1, 2, 3, 4, 5, 6, 7, 8, 10]
    """
    print("P5 — Fusionar dos listas ordenadas sin sort")
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8, 10]
    fusion = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            fusion.append(a[i])
            i = i + 1
        else:
            fusion.append(b[j])
            j = j + 1
    fusion.extend(a[i:])
    fusion.extend(b[j:])
    print("Manual: Fusión con dos índices:", fusion)
    print("Python: Comprobación:", sorted(a + b))


# ============================== CATÁLOGO =============================
#  (código, título, tipo, función)   ->  tipo: "taller" o "propuesto"
#  ✅ Ya está armado: NO lo cambies, úsalo en menu_ejercicios().
EJERCICIOS = [
    ("T1", "CRUD de pasajeros con clase Pasajero + list", "taller", ejercicio_t1),
    ("T2", "Estadísticas de una lista de notas",          "taller", ejercicio_t2),
    ("T3", "Ordenar una lista (bubble sort)",             "taller", ejercicio_t3),
    ("P1", "Contar apariciones de un valor",              "propuesto", ejercicio_p1),
    ("P2", "Invertir una lista",                          "propuesto", ejercicio_p2),
    ("P3", "Números únicos",                              "propuesto", ejercicio_p3),
    ("P4", "Segundo mayor",                               "propuesto", ejercicio_p4),
    ("P5", "Fusionar dos listas ordenadas",               "propuesto", ejercicio_p5),
]


def menu_ejercicios():
    """
    QUÉ HACE : muestra los ejercicios agrupados y ejecuta el que elija
               el usuario, hasta que escriba 0.
    PASOS    :
      1. Con COMPRENSIONES separa el catálogo:
             taller     = [e for e in EJERCICIOS if e[2] == "taller"]
             propuestos = [e for e in EJERCICIOS if e[2] == "propuesto"]
      2. Muestra:
             --- DESARROLLADOS (taller) ---
               T1. CRUD de pasajeros ...
             --- PROPUESTOS ---
               P1. Contar apariciones ...
               0.  Volver
      3. Lee el código (ej. "t2") y pásalo a mayúsculas con .upper().
      4. Busca la tupla con ese código (otra comprensión o next(...)):
             encontrados = [e for e in EJERCICIOS if e[0] == codigo]
      5. Si existe -> llama a su función:  encontrados[0][3]()
         Si no     -> "Código no válido".
      6. Repite hasta que el usuario escriba "0".
    """
    taller = [e for e in EJERCICIOS if e[2] == "taller"]
    propuestos = [e for e in EJERCICIOS if e[2] == "propuesto"]

    while True:
        print("\n--- DESARROLLADOS (taller) ---")
        for codigo, titulo, tipo, funcion in taller:
            print(f"  {codigo}. {titulo}")
        print("--- PROPUESTOS ---")
        for codigo, titulo, tipo, funcion in propuestos:
            print(f"  {codigo}. {titulo}")
        print("  0. Volver")

        codigo = input("Código: ").strip().upper()
        if codigo == "0":
            break
        encontrados = [e for e in EJERCICIOS if e[0] == codigo]
        if encontrados:
            encontrados[0][3]()
        else:
            print("  Código no válido")
