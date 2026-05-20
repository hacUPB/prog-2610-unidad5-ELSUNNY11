# Analizador de Calidad del Aire y Climatología (TXT y CSV)

Este proyecto es una herramienta en consola desarrollada en Python que permite explorar carpetas, procesar reportes de texto (`.txt`) y analizar bases de datos meteorológicas (`.csv`) de forma nativa (sin usar librerías como Pandas). Además, genera gráficos automáticos utilizando `matplotlib`.

---

## Cómo usarlo

1. **Instala la librería para los gráficos:**
   bash
   pip install matplotlib

Ejecuta el programa:
Coloca tus archivos (datos_calidad_aire_texto.txt y Normales_climatológicas_del_Ozono_20251028.csv) en la misma u otra carpeta que main.py y arranca el script:

Bash
python main.py
Flujo de trabajo:

Selecciona la Opción 1 pega la ruta de tu carpeta \data para escanear la ruta de tu carpeta. El programa listará tus archivos con un número asignado.

Entra al submenú de TXT o CSV según corresponda e ingresa el número del archivo.

Los gráficos que elijas generar se guardarán automáticamente en la carpeta ./outputs/.

Análisis y Casos de Estudio Reales
1. Reportes de Calidad del Aire (datos_calidad_aire_texto.txt)
Al pasar el archivo de texto por el programa, podemos auditar registros ambientales y alertas:

Conteo y Lectura: Calcula en segundos el total de líneas, palabras y caracteres del reporte.

Búsqueda de Patrones: Rastrea automáticamente alertas críticas buscando la palabra ERROR (para fallas en los sensores de medición) o códigos como 404.

Detección de Fechas: Encuentra y extrae las fechas exactas en las que se registraron las mediciones de partículas o gases contaminantes.

2. Climatología del Ozono (Normales_climatológicas_del_Ozono_20251028.csv)
Procesar este dataset histórico

Estadísticas de Columna: Permite elegir la columna para calcular instantáneamente el promedio de contaminación, el valor máximo registrado (picos de polución) y la mediana de los datos.

Visualización de Tendencias: * Con el Gráfico de Líneas, se puede observar la evolución a lo largo del tiempo o los meses.

El Gráfico de Dispersión (Scatter) ayuda a entender si el aumento de la radiación solar o la temperatura afecta directamente los niveles de Ozono en el aire.

🧬 Características del Código
Procesamiento Puro: Todo el filtrado de texto, la separación de columnas por comas (CSV) y la limpieza de caracteres especiales se programaron desde cero de forma nativa.

Algoritmos Manuales: Implementa bucles lógicos propios para ordenar las palabras más frecuentes y realizar el cálculo de la mediana matemática sin depender de herramientas externas.