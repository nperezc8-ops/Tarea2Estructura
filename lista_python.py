# =====================================================================
#  lista_python.py  —  LISTA 2: con el list de PYTHON (built-in)
# ---------------------------------------------------------------------
#  Mismas operaciones que la Lista 1, pero ahora usamos lo que Python
#  ya trae: append, insert, pop, remove, sort, reverse, copy, len,
#  enumerate, next, bisect ... y LIST COMPREHENSIONS.
#
#      self.pasajeros -> [Pasajero, Pasajero, ...]   (crece sola)
#
#  ✅ OBLIGATORIO usar comprensiones de listas en (mínimo):
#       buscar · buscar_binaria · eliminar_por_valor (versión 2)
#       filtrar_mayores_de_edad · nombres_en_mayusculas
#
#  Recordatorio de la sintaxis:
#       [EXPRESIÓN for ELEMENTO in LISTA]            -> transformar
#       [ELEMENTO  for ELEMENTO in LISTA if COND]    -> filtrar
#       [EXPRESIÓN for ELEMENTO in LISTA if COND]    -> las dos a la vez
#
#  📌 Compara cada método con su gemelo de lista_manual.py:
#     allá eran 10 líneas, aquí casi siempre son 1 o 2.

# =====================================================================

from bisect import bisect_left
from pasajero import Pasajero


class ListaPasajerosPython:

    def __init__(self):
        # Versión manual: 3 líneas de código, sin firma ni docstring.
        self.pasajeros = []               # list de Python: crece sola

    # -----------------------------------------------------------------
    # 1. AÑADIR  ✅ YA RESUELTO
    # -----------------------------------------------------------------
    def añadir(self, pasajero):
        """Añade al final con append()."""
        # Versión manual: 9 líneas de código, sin firma ni docstring.
        if self.buscar(pasajero.cedula) != -1:
            print("  Esa cédula ya está registrada")
            return False
        self.pasajeros.append(pasajero)
        return True

    # -----------------------------------------------------------------
    # 2. LISTAR  ✅ YA RESUELTO
    # -----------------------------------------------------------------
    def listar(self):
        """Muestra los pasajeros con su posición usando enumerate()."""
        # Versión manual: 5 líneas de código, sin firma ni docstring.
        if not self.pasajeros:                  # lista vacía es False
            print("(lista vacía)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"[{i}] {p}")

    # -----------------------------------------------------------------
    # 3. LONGITUD
    # -----------------------------------------------------------------
    def longitud(self):
        """
        USA      : len()
        RETORNA  : int.   PRUEBA: datos de prueba -> 5
        """
        # Versión manual: 1 línea de código, sin firma ni docstring.
        return len(self.pasajeros)

    # -----------------------------------------------------------------
    # 4. INSERTAR
    # -----------------------------------------------------------------
    def insertar(self, posicion, pasajero):
        """
        USA      : self.pasajeros.insert(posicion, pasajero)
        VALIDA   : 0 <= posicion <= len(self.pasajeros); si no, mensaje y False.
        PIENSA   : ¿por qué ya no tienes que correr nada a la derecha?
                   (Python lo hace por ti... pero lo sigue haciendo: O(n)).
        """
        # Versión manual: 16 líneas de código, sin firma ni docstring.
        # Python también desplaza los elementos para abrir espacio.
        # En el peor caso, insertar requiere O(n) desplazamientos.
        if posicion < 0 or posicion > len(self.pasajeros):
            print("  Posición no válida")
            return False
        if self.buscar(pasajero.cedula) != -1:
            print("  Esa cédula ya está registrada")
            return False
        self.pasajeros.insert(posicion, pasajero)
        return True

    # -----------------------------------------------------------------
    # 5. BUSCAR POR CÉDULA  (con COMPRENSIÓN)
    # -----------------------------------------------------------------
    def buscar(self, cedula):
        """
        RETORNA  : la posición (int) o -1.
        USA      : una comprensión con enumerate que junte las posiciones
                   que coinciden:
                       posiciones = [i for i, p in enumerate(self.pasajeros)
                                     if p.cedula == cedula]
                   Si la lista 'posiciones' está vacía -> -1,
                   si no -> posiciones[0].
        EXTRA    : investiga la versión con next(...):
                   next((i for i, p in enumerate(...) if ...), -1)
        PRUEBA   : buscar("0987654321") -> 2 ;  buscar("1111111111") -> -1
        """
        # Versión manual: 4 líneas de código, sin firma ni docstring.
        posiciones = [i for i, p in enumerate(self.pasajeros) if p.cedula == cedula]
        if not posiciones:
            return -1
        return posiciones[0]

    # -----------------------------------------------------------------
    # 6. BUSCAR BINARIA  (con COMPRENSIÓN + bisect)
    # -----------------------------------------------------------------
    def buscar_binaria(self, cedula):
        """
        ⚠ REQUISITO: lista ordenada por cédula (ordenar_asc antes).
        PASOS    :
          1. cedulas = [p.cedula for p in self.pasajeros]   # COMPRENSIÓN
          2. i = bisect_left(cedulas, cedula)   # dónde "debería" estar
          3. Si i < len(cedulas) y cedulas[i] == cedula -> return i
          4. return -1
        PRUEBA   : datos ordenados -> buscar_binaria("0923456789") -> 2
        """
        # Versión manual: 15 líneas de código, sin firma ni docstring.
        cedulas = [p.cedula for p in self.pasajeros]
        for i in range(len(cedulas) - 1):
            if cedulas[i] > cedulas[i + 1]:
                print("  La lista no está ordenada. Use primero la opción 9.")
                return -1

        i = bisect_left(cedulas, cedula)
        if i < len(cedulas) and cedulas[i] == cedula:
            return i
        return -1

    # -----------------------------------------------------------------
    # 7. MODIFICAR
    # -----------------------------------------------------------------
    def modificar(self, cedula, nuevo_nombre, nueva_edad):
        """
        PASOS    : pos = self.buscar(cedula); si -1 -> False;
                   si no, cambia self.pasajeros[pos].nombre y .edad -> True
        """
        # Versión manual: 7 líneas de código, sin firma ni docstring.
        pos = self.buscar(cedula)
        if pos == -1:
            print("  No existe esa cédula")
            return False
        self.pasajeros[pos].nombre = nuevo_nombre
        self.pasajeros[pos].edad = nueva_edad
        return True

    # -----------------------------------------------------------------
    # 8. ELIMINAR POR POSICIÓN
    # -----------------------------------------------------------------
    def eliminar_por_posicion(self, posicion):
        """
        USA      : self.pasajeros.pop(posicion)   (retorna el eliminado)
        VALIDA   : 0 <= posicion < len(...); si no -> mensaje y None
        """
        # Versión manual: 9 líneas de código, sin firma ni docstring.
        if posicion < 0 or posicion >= len(self.pasajeros):
            print("  Posición no válida")
            return None
        return self.pasajeros.pop(posicion)

    # -----------------------------------------------------------------
    # 9. ELIMINAR POR VALOR (por cédula)  — hazlo de DOS formas
    # -----------------------------------------------------------------
    def eliminar_por_valor(self, cedula):
        """
        FORMA 1 (remove):
            pos = self.buscar(cedula) ... self.pasajeros.remove(self.pasajeros[pos])
        FORMA 2 (COMPRENSIÓN) — la que debe quedar activa:
            antes = len(self.pasajeros)
            self.pasajeros = [p for p in self.pasajeros if p.cedula != cedula]
            return len(self.pasajeros) < antes      # True si eliminó algo
        Deja la FORMA 1 comentada para comparar.
        """
        # Versión manual: 6 líneas de código, sin firma ni docstring.
        # FORMA 1: alternativa con remove, comentada para comparar.
        # pos = self.buscar(cedula)
        # if pos == -1:
        #     print("  No existe esa cédula")
        #     return False
        # self.pasajeros.remove(self.pasajeros[pos])
        # return True
        # FORMA 2: la comprensión queda activa.
        antes = len(self.pasajeros)
        self.pasajeros = [p for p in self.pasajeros if p.cedula != cedula]
        if len(self.pasajeros) == antes:
            print("  No existe esa cédula")
            return False
        return True

    # -----------------------------------------------------------------
    # 10. ORDENAR ASCENDENTE (por cédula)
    # -----------------------------------------------------------------
    def ordenar_asc(self):
        """
        USA      : self.pasajeros.sort(key=lambda p: p.cedula)
        PIENSA   : ¿qué hace key=? ¿qué pasaría sin él? (pruébalo)
        """
        # Versión manual: 7 líneas de código, sin firma ni docstring.
        # key indica que se comparan las cédulas y no los objetos Pasajero.
        # Sin key, ordenar varios Pasajero produce TypeError: no tienen un orden definido.
        self.pasajeros.sort(key=lambda p: p.cedula)

    # -----------------------------------------------------------------
    # 11. ORDENAR DESCENDENTE (por cédula)
    # -----------------------------------------------------------------
    def ordenar_desc(self):
        """ USA : sort(key=..., reverse=True) """
        # Versión manual: 7 líneas de código, sin firma ni docstring.
        self.pasajeros.sort(key=lambda p: p.cedula, reverse=True)

    # -----------------------------------------------------------------
    # 12. REVERSAR
    # -----------------------------------------------------------------
    def reversar(self):
        """ USA : self.pasajeros.reverse()   (no es lo mismo que ordenar_desc) """
        # Versión manual: 8 líneas de código, sin firma ni docstring.
        self.pasajeros.reverse()

    # -----------------------------------------------------------------
    # 13. COPIAR
    # -----------------------------------------------------------------
    def copiar(self):
        """
        PASOS    :
          nueva = ListaPasajerosPython()
          nueva.pasajeros = self.pasajeros.copy()    # o self.pasajeros[:]
          return nueva
        ⚠ OJO    : es una copia SUPERFICIAL: las dos listas son distintas,
                   pero los objetos Pasajero de adentro son los MISMOS.
                   Reversar la copia no afecta al original;
                   modificar un pasajero de la copia... ¡sí! Pruébalo.
        """
        # Versión manual: 4 líneas de código, sin firma ni docstring.
        # La copia es superficial: el contenedor es nuevo, pero comparte los pasajeros.
        # Reversar la copia no cambia el orden del original.
        # Modificar un pasajero de la copia sí cambia ese objeto también en el original.
        nueva = ListaPasajerosPython()
        nueva.pasajeros = self.pasajeros.copy()
        return nueva

    # -----------------------------------------------------------------
    # 14. FILTRAR MAYORES DE EDAD  (COMPRENSIÓN que FILTRA)
    # -----------------------------------------------------------------
    def filtrar_mayores_de_edad(self):
        """
        RETORNA  : una NUEVA ListaPasajerosPython.
        PASOS    :
          nueva = ListaPasajerosPython()
          nueva.pasajeros = [p for p in self.pasajeros if p.es_mayor_de_edad()]
          return nueva
        PRUEBA   : datos de prueba -> todos menos Beto
        """
        # Versión manual: 5 líneas de código, sin firma ni docstring.
        nueva = ListaPasajerosPython()
        nueva.pasajeros = [p for p in self.pasajeros if p.es_mayor_de_edad()]
        return nueva

    # -----------------------------------------------------------------
    # 15. NOMBRES EN MAYÚSCULAS  (COMPRENSIÓN que TRANSFORMA)
    # -----------------------------------------------------------------
    def nombres_en_mayusculas(self):
        """
        RETORNA  : list de str ->  [p.nombre.upper() for p in self.pasajeros]
        PRUEBA   : ['DIANA', 'ANA', 'LUIS', 'BETO', 'ELENA']
        """
        # Versión manual: 4 líneas de código, sin firma ni docstring.
        return [p.nombre.upper() for p in self.pasajeros]
