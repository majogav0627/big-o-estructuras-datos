# Resultados y Análisis de Complejidad - Big O

## 1. Tabla de Tiempos por Tamaño de Muestra (n)
*Mediciones obtenidas mediante `time.perf_counter()` a partir de los datos en GitHub.*

| n (Registros) | List O(n) | Set O(1) prom. | Dict O(1) prom. |
|---|---|---|---|
| 100 | 0.000005 s | 0.000001 s | 0.000001 s |
| 1,000 | 0.000045 s | 0.000001 s | 0.000001 s |
| 10,000 | 0.000412 s | 0.000002 s | 0.000001 s |
| 50,000 | 0.002150 s | 0.000002 s | 0.000002 s |
| 100,000 | 0.009404 s | 0.000004 s | 0.000002 s |

---

## 2. Respuestas a las Preguntas de Análisis Obligatorias

1. **¿Por qué una búsqueda secuencial sobre List se clasifica como O(n)?**
   Porque en el peor de los casos (elemento al final o inexistente), requiere examinar cada uno de los elementos de la lista de forma consecutiva, haciendo que el tiempo crezca linealmente con respecto al tamaño del conjunto ($n$).

2. **¿Por qué Set y Dictionary tienen búsqueda O(1) en promedio?**
   Utilizan funciones de *hashing* para calcular directamente la dirección de memoria de la llave, evitando tener que recorrer toda la colección elemento por elemento.

3. **¿Por qué O(1) no significa “cero tiempo” ni “exactamente el mismo tiempo siempre”?**
   Porque la notación Big O describe el comportamiento asintótico de crecimiento, no los nanosegundos físicos reales. Siempre existirá un costo computacional constante influenciado por el hardware y colisiones de hash.

4. **¿Cuál es la diferencia entre medir segundos y analizar Big O?**
   Los segundos reflejan el rendimiento empírico en un equipo y entorno particulares, mientras que Big O es un análisis matemático abstracto de cómo escala el algoritmo a medida que $n$ crece hacia el infinito.

5. **¿Por qué una lista enlazada puede insertar al inicio en O(1) pero buscar en O(n)?**
   Insertar al inicio solo exige modificar el puntero de la cabeza, lo cual es inmediato. Buscar exige un recorrido nodo a nodo mediante referencias, ya que las listas enlazadas carecen de índices directos.

6. **¿Qué condición permite que un árbol de búsqueda se acerque a O(log n)?**
   Que el Árbol Binario de Búsqueda (BST) permanezca balanceado, asegurando que en cada paso de comparación se descarte aproximadamente la mitad de los nodos restantes.

7. **¿Qué ocurre con el BST si se inserta información ya ordenada?**
   El árbol se degenera adoptando una forma lineal idéntica a una lista enlazada, degradando su rendimiento de búsqueda al peor caso: $O(n)$.

8. **¿Qué estructura elegiría para recuperar un estudiante completo por carnet? Justifique.**
   Un **Dictionary**, porque asocia directamente la clave única (carnet) con el objeto completo del registro, permitiendo recuperaciones instantáneas en tiempo promedio $O(1)$.

9. **¿Qué estructura elegiría si solamente necesita saber si un carnet existe? Justifique.**
   Un **Set**, ya que está diseñado precisamente para evaluar pertenencia de elementos únicos de forma sumamente eficiente $O(1)$ promedio y con menor sobrecarga que almacenar un diccionario completo.

10. **Si el sistema realiza 70% búsquedas, 20% inserciones y 10% reportes, qué decisión de diseño tomaría y por qué?**
    Con un volumen tan abrumador de búsquedas, un **Dictionary** es ideal debido a sus consultas $O(1)$. No obstante, si las inserciones fueran masivas y desordenadas, convendría evaluar estructuras indexadas que soporten modificaciones frecuentes sin penalizar gravemente la lectura.

---

## 3. Conclusión Técnica
La elección de una estructura de datos nunca debe ser arbitraria; depende directamente de las operaciones predominantes del sistema y de su escalabilidad ante grandes volúmenes de información. Mientras que las colecciones secuenciales como listas y listas enlazadas sufren caídas severas de rendimiento al escalar a millones de registros ($O(n)$), las estrategias basadas en tablas hash (`Set` y `Dict`) garantizan un comportamiento eficiente y constante ($O(1)$). Comprender la notación Big O permite tomar decisiones de arquitectura sólidas antes de que el crecimiento de los datos comprometa la estabilidad del sistema.

## Declaración de uso de Inteligencia Artificial
En el desarrollo de este laboratorio, se empleó un modelo de Inteligencia Artificial (Google Gemini) como herramienta de apoyo pedagógico, consulta técnica y estructuración de código base. La herramienta fue utilizada para:
- Comprender la lógica de consumo de archivos CSV mediante URLs RAW en Python.
- Verificar la correcta implementación teórica de las complejidades en notación Big O (`O(n)`, `O(1)`, `O(\log n)`).
- Organizar la redacción técnica del análisis y las respuestas obligatorias.

Toda la implementación, ejecución de pruebas en entorno local, validación de tiempos con `time.perf_counter()`, control de versiones en Git y subida al repositorio final fueron revisadas, probadas y validadas por el equipo de trabajo.