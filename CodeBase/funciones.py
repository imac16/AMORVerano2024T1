def generar_tabla_distribucion_frecuencias(datos, lim_inf, lim_sup, marcas_clase, fa, fr, fatum):


  # Encabezado de la tabla
  encabezado = "| N°| LimInf | LimSup | MarcaC |fa |   fr   | Facum  |\n"
  linea_divisoria = "|---|--------|--------|--------|---|--------|--------|\n"

  # Cuerpo de la tabla
  cuerpo_tabla = ""
  for i, (clase, lim_inf_valor, lim_sup_valor, marca_clase_valor, fa_valor, fr_valor, fatum_valor) in enumerate(zip(range(1, len(lim_inf) + 1), lim_inf, lim_sup, marcas_clase, fa, fr, fatum)):
    fila = f"| {clase} | {lim_inf_valor:.4f} | {lim_sup_valor:.4f} | {marca_clase_valor:.4f} | {fa_valor:.0f} | {fr_valor:.2f}% | {fatum_valor:.2f}% |\n"
    cuerpo_tabla += fila

  # Tabla completa
  tabla_completa = encabezado + linea_divisoria + cuerpo_tabla + linea_divisoria

  return tabla_completa

def sort_clases_fa(clases_originales, clases_sorted, fa_absolutas):
    '''
    Regresa lista de frecuencias absolutas ordenadas
    
    Ejemplo:    
    clases_originales = [0, 5, 7, 6, 4, 2]
    clases_sorted = [0, 2, 4, 5, 6, 7]
    fa_absolutas = [2, 3, 2, 1, 1, 2]
    fa_sorted = sort_clases_fa(clases_originales, clases_sorted, fa_absolutas):
    >>> [2, 2, 1, 3, 1, 2] 
    '''

    fa_sorted = []
    for elemento in clases_sorted:
        idx = clases_originales.index(elemento)
        fa = fa_absolutas[idx]
        fa_sorted.append(fa)

    return fa_sorted

def formateando_str(nombres):
  """
  Función que quita los acentos y convierte a mayúsculas los elementos de un arreglo de nombres.

  Argumentos:
    nombres (list): El arreglo de nombres a formatear.

  Retorna:
    list: El arreglo de nombres formateado sin acentos y en mayúsculas.
  """

  # Diccionario de traducción de caracteres acentuados a sin acentos
  diccionario_acentos = {
      "á": "A",
      "é": "E",
      "í": "I",
      "ó": "O",
      "ú": "U"
  }
  nombres_formateados = []
  for nombre in nombres:
    nombre_sin_acentos = nombre.translate(str.maketrans(diccionario_acentos))

    nombre_final = nombre_sin_acentos.upper().replace(" ", "").strip()

    nombres_formateados.append(nombre_final)

  return nombres_formateados


def ordenar_asc(arreglo):
    '''
    Regresa el arreglo ordenado de forma
    ascendente.
    
    Ejemplo:
    arreglo = [0, 5, 7, 6, 4, 2]
    arr_sorted = ordenar_asc(arreglo)
    >>> [0, 2, 4, 5, 6, 7]
    '''
    arr_len = len(arreglo)

    for i in range(arr_len):
        min_idx = i
        for j in range(i+1, arr_len):
            if arreglo[j] < arreglo[min_idx]:
                min_idx = j
        arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]         

    return arreglo

    import pandas as pd

def imptabla(clases, frec_absoluta, frec_relativa, frec_rel_acumulada):


  # Crear el DataFrame
  df = pd.DataFrame({
      
    "Clases": clases,
    "Frecuencia absoluta": frec_absoluta,
    "Frecuencia relativa": frec_relativa,
    "Frecuencia relativa acumulada": frec_rel_acumulada
  })

  # Mostrar la tabla
  print(df.to_string())

def fa_grouped(numeros, lim_inf, lim_sup):

  # Inicializar la lista de frecuencias
  frecuencias = [0] * len(lim_inf)

  # Contar las frecuencias para cada clase
  for numero in numeros:
    # Recorrer las clases
    for i, (limite_inf, limite_sup) in enumerate(zip(lim_inf, lim_sup)):
      # Si el número está dentro del intervalo (inclusivo para la última clase)
      if (limite_inf <= numero <= limite_sup) or (i == len(lim_inf) - 1 and numero == limite_sup):
        frecuencias[i] += 1
        break  # No es necesario seguir recorriendo si el número ya está en una clase

  return frecuencias

def ordenar_cadenas(cadenas_formateadas):

  for i in range(len(cadenas_formateadas)):
    for j in range(i + 1, len(cadenas_formateadas)):
      if cadenas_formateadas[i] > cadenas_formateadas[j]:
        cadenas_formateadas[i], cadenas_formateadas[j] = cadenas_formateadas[j], cadenas_formateadas[i]

  return cadenas_formateadas

def obtener_indices(arreglo_entrada):
  arreglo_salida = []  
  for i, elemento in enumerate(arreglo_entrada):
    indice = arreglo_entrada.index(elemento)
    indice += 1
      
    arreglo_salida.append(indice)
  return arreglo_salida

def obtener_frecuencia_relativa_acumulada(fr):
    frecuencias_acumuladas = []
    suma = 0
    for elemento in fr:
        suma += elemento
        frecuencias_acumuladas.append(suma)
    return frecuencias_acumuladas

import math
import numpy as np

import numpy as np

def calcular_estadisticas_intervalos(numeros):

  # Cálculo del rango
  rango = np.max(numeros) - np.min(numeros)

  # Cálculo del número de clases (Sturges)
  num_clases = 1 + 3.3 * np.log10(len(numeros))
  parte_entera = int(num_clases)
  parte_decimal = num_clases - parte_entera

  if parte_decimal < 0.5:
    # Redondear hacia abajo
    num_clases= parte_entera
  else:
    # Redondear hacia arriba
    num_clases= parte_entera + 1

  # Cálculo del ancho de clase
  ancho_clase = rango / num_clases

  # Definición de los límites de clase
  limites_clases = []
  limite_inferior_A=[]
  limite_superior_A=[]
    
   
  for i in range(int(num_clases)):
    limite_inferior = np.min(numeros) + i * ancho_clase
    limite_superior = limite_inferior + ancho_clase
    limites_clases.append((limite_inferior, limite_superior))
    limite_inferior_A.append(limite_inferior)
    limite_superior_A.append(limite_superior)

  # Cálculo de las marcas de clase
  marcas_clases = []
  for limite_inferior, limite_superior in limites_clases:
    marca_clase = (limite_inferior + limite_superior) / 2
    marcas_clases.append(marca_clase)

  return limite_inferior_A, limite_superior_A, marcas_clases



import matplotlib.pyplot as plt
def generar_diagrama_barras_horizontal(fa_sorted, clases_sorted, marcas_clase, labelx, labely, titulo):
    """
    Genera un diagrama de barras horizontales con las características especificadas.

    Argumentos:
        fa_sorted: Lista con las frecuencias absolutas ordenadas para el eje Y.
        clases_sorted: Lista con los nombres de las clases (textos para las marcas del eje X).

    """
    # Configurar figura y tamaño
    plt.figure(figsize = (12, 6))

    # Diagrama de barras horizontales con:
    # - Barras ajustadas al 100% de altura (height = 0.8)
    # - Contorno negro (edgecolor = "k")
    # - Colores específicos para cada barra
    plt.barh(marcas_clase, fa_sorted, height=0.8, edgecolor="k",
            color=["#FF5733", "#33FFF3", "#FF33F9", "#3339FF", "#E6FF33", "#FF3346"])

    # Personalizar marcas del eje Y (inclinadas 45°) y tamaño de fuente
    plt.yticks(marcas_clase, clases_sorted, fontsize=15, rotation=45)

    # Etiquetas y título del gráfico con tamaño de fuente grande
    plt.ylabel(labelx, fontsize = 25)  # Etiqueta del eje Y
    plt.xlabel(labely, fontsize = 25)  # Etiqueta del eje X
    plt.title(titulo, fontsize = 40)

    # Activar cuadrícula
    plt.grid()

    # Mostrar el gráfico
    plt.show()


import matplotlib.pyplot as plt
def generar_histograma(marcas_clase, frecuencia, clases_sorted, labelx, labely, titulo):
    """
    Genera un histograma con las características especificadas.

    Argumentos:
        marcas_clase: Lista con las marcas de clase para el eje X.
        frecuencia: Lista con las frecuencias absolutas para el eje Y.
        clases_sorted: Lista con los nombres de las clases (textos para las marcas).

    """
    # Configurar figura y tamaño
    plt.figure(figsize = (12, 6))

    # Histograma con barras ajustadas al 100%, contorno negro y colores específicos
    plt.bar(marcas_clase, frecuencia, width=1, edgecolor="k",
            color = ["#FF5733", "#33FFF3", "#FF33F9", "#3339FF", "#E6FF33", "#FF3346"])

    # Personalizar marcas del eje X (inclinadas 45°) y tamaño de fuente
    plt.xticks(marcas_clase, clases_sorted, fontsize=15, rotation=45)

    # Etiquetas y título del gráfico con tamaño de fuente grande
    plt.xlabel(labelx, fontsize = 25)
    plt.ylabel(labely, fontsize = 25)
    plt.title(titulo, fontsize = 40)

    # Activar cuadrícula
    plt.grid()

    # Mostrar el gráfico
    plt.show()

    import matplotlib.pyplot as plt
def generar_ojiva(marcas_clase, frecuencia_relativa_acumulada, clases_sorted, labelx, labely, titulo):
    plt.figure(figsize = (12, 6)) # (ancho, alto) del grafico
    frecuencia = frecuencia_relativa_acumulada # Datos del eje y
    
    # Ajuste a las listas para generar el poligono de frecuencias
    datos_x = [0] + marcas_clase  
    datos_y = [0] + frecuencia 
    
    #leyendas para las marcas de clase
    marcas_textos = clases_sorted
    
    # Poligono de frecuencias con:
    # - Estilo de linea punteado (lenestyle ":"). https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
    # - Marcador con forma triangular (marker = "v"). https://matplotlib.org/stable/api/markers_api.html
    
    plt.plot(datos_x , datos_y, 
    linewidth = 5, color = "r", linestyle = ":",
    marker = "v", markersize = 15, markeredgecolor = "#FF33F9", markerfacecolor = "#33FFF3") 
    
    plt.xticks(marcas_clase , marcas_textos, fontsize = 15, rotation = 45) # Cambio de las marcas del eje x de numeros a texto
    plt.xlabel(labelx, fontsize = 25) # Etiqueta del eje x
    plt.ylabel(labely, fontsize = 25) # Etiqueta del eje y
    plt.title(titulo, fontsize = 40) # Titulo
    plt.grid() # Se activa la cuadricula
    plt.show() # Se muestra el grafico en pantalla 


import matplotlib.pyplot as plt
def generar_pastel(clases_sorted, datos, titulo):
    plt.pie(datos, 
            labels = clases_sorted,
            colors = [ "#33FFF3", "#FF33F9", "#3339FF","#FF5733", "#E6FF33", "#FF3346"],
            autopct = "%0.01f%%",
            pctdistance = 0.8,
            counterclock = False,
            startangle = 90
           )
    plt.title(titulo, fontsize=40)
    plt.show() 


import matplotlib.pyplot as plt
def generar_poligono_frecuencias(frecuencia_relativa, clases_sorted, marcas_clase, labelx, labely, titulo):
    plt.figure(figsize = (12, 6)) # (ancho, alto) del grafico
    frecuencia = frecuencia_relativa # Datos del eje y
    

    # Ajuste a las listas para generar el poligono de frecuencias
    datos_x = [0] + marcas_clase + [len(clases_sorted)+1] 
    datos_y = [0] + frecuencia + [0] 
    
    #leyendas para las marcas de clase
    marcas_textos = clases_sorted
    
    # Poligono de frecuencias con:
    # - Estilo de linea punteado (lenestyle ":"). https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
    # - Marcador con forma triangular (marker = "v"). https://matplotlib.org/stable/api/markers_api.html
    
    plt.plot(datos_x , datos_y, 
            linewidth = 5, color = "r", linestyle = ":",
            marker = "v", markersize = 15, markeredgecolor = "#FF33F9", markerfacecolor = "#33FFF3") 
    
    plt.xticks(marcas_clase , marcas_textos, fontsize = 15, rotation = 45) # Cambio de las marcas del eje x de numeros a texto
    plt.xlabel(labelx, fontsize = 25) # Etiqueta del eje x
    plt.ylabel(labely, fontsize = 25) # Etiqueta del eje y
    plt.title(titulo, fontsize = 40) # Titulo
    plt.grid() # Se activa la cuadricula
    plt.show() # Se muestra el grafico en pantalla

def obtener_frecuencia_relativa(arreglo):
  """
  Función para obtener la frecuencia relativa de los elementos en un arreglo.
  """
  # Calcular la frecuencia relativa para cada elemento
    
  frecuencia_relativa = []
  for elemento in arreglo:
      
    frecuencia_relativa.append(elemento / sum(arreglo)*100)
  return frecuencia_relativa

import pandas as pd

def generar_tabla(clases, frec_absoluta, frec_relativa, frec_rel_acumulada):
  """
  Función que genera una tabla con datos de clases, frecuencias absolutas, frecuencias relativas y frecuencias relativas acumuladas.

  Parámetros:
    clases: Lista con las etiquetas de las clases.
    frec_absoluta: Lista con las frecuencias absolutas de cada clase.
    frec_relativa: Lista con las frecuencias relativas de cada clase.
    frec_rel_acumulada: Lista con las frecuencias relativas acumuladas de cada clase.

  Retorno:
    DataFrame: Un DataFrame de Pandas con los datos tabulados.
  """

  # Crear el DataFrame
  df = pd.DataFrame({
    "Clases": clases,
    "Frecuencia absoluta": frec_absoluta,
    "Frecuencia relativa": frec_relativa,
    "Frecuencia relativa acumulada": frec_rel_acumulada
  })

  # Mostrar la tabla
  print(df.to_string())


def frec_abs(datos_entrada):
    '''
    clases, fa_absoluta = frec_abs(datos_entrada)
    Regresa las clases y frecuencias absolutas 
    de cada clase dada una lista de datos

    Ejemplo:
    datos_entrada = [0, 1, 2, 0, 1, 3, 1, 3]
    clases, fa_absoluta= frec_abs(datos_entrada)
    >>>clases[0, 1, 2, 3]
    >>> fa_absoluta[2, 3, 1, 2]
    
    '''
    clases, fa_absoluta = [],[]
    for elemento in datos_entrada:
        if elemento not in clases:
            clases.append(elemento)
            fa_absoluta.append(1)
        else:        
            idx = clases.index(elemento)        
            fa_absoluta[idx] += 1 
    return clases, fa_absoluta
        

