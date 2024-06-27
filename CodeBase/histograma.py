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