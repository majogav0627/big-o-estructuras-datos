import csv
import time
import urllib.request
from lista_enlazada import ListaEnlazada
from arbol_bst import ArbolBST

# Reemplazarás esta URL con tu enlace RAW de GitHub en el siguiente paso
URL = "https://raw.githubusercontent.com/majogav0627/big-o-estructuras-datos/a7eced21d1efa525e64f5d9cfeb1eb4b9b02a704/data/estudiantes.csv"

def descargar_datos(url):
    print("Descargando datos desde GitHub...")
    respuesta = urllib.request.urlopen(url)
    lineas = [linea.decode('utf-8') for linea in respuesta.readlines()]
    lector = csv.DictReader(lineas)
    return list(lector)
    
def buscar_lista(estudiantes, carnet):
    for estudiante in estudiantes:
        if estudiante["carnet"] == carnet:
            return estudiante
    return None

if __name__ == "__main__":
    try:
        estudiantes = descargar_datos(URL)
        print(f"OK: {len(estudiantes):,} registros recibidos.")

        # Seleccionar un carnet de prueba ubicado al final (peor caso para O(n))
        carnet_objetivo = estudiantes[-1]["carnet"]

        print("\n--- Probando List, Set, Dictionary ---")
        
        # 1. Medir Lista O(n)
        inicio = time.perf_counter()
        res_lista = buscar_lista(estudiantes, carnet_objetivo)
        tiempo_lista = time.perf_counter() - inicio

        # Crear estructuras de acceso rápido O(1) promedio
        carnets_set = {e["carnet"] for e in estudiantes}
        estudiantes_dict = {e["carnet"]: e for e in estudiantes}

        # 2. Medir Set O(1)
        inicio = time.perf_counter()
        res_set = carnet_objetivo in carnets_set
        tiempo_set = time.perf_counter() - inicio

        # 3. Medir Dict O(1)
        inicio = time.perf_counter()
        res_dict = estudiantes_dict.get(carnet_objetivo)
        tiempo_dict = time.perf_counter() - inicio

        print(f"List Tiempo: {tiempo_lista:.8f} s (Encontrado: {res_lista is not None})")
        print(f"Set  Tiempo: {tiempo_set:.8f} s (Encontrado: {res_set})")
        print(f"Dict Tiempo: {tiempo_dict:.8f} s (Encontrado: {res_dict is not None})")

    except Exception as e:
        print(f"Error: {e}")
        