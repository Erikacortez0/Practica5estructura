def ingresar_datos():
    n = int(input("Ingrese una cantidad de datos: "))
    datos = []
    for i in range(n):
        dato = float(input(f"Ingrese un dato {i + 1}: "))
        datos.append(dato)
    return datos

def ordenar_lista(datos):
    n = len(datos)
    for i in range(n):
        for j in range(0, n-i-1):
            if datos[j] > datos[j+1]:
                datos[j], datos[j+1] = datos[j+1], datos[j]
    return datos

def calcular_sumatoria(datos):
    suma = 0
    for dato in datos:
        suma += dato
    return suma

def calcular_media(datos):
    suma = calcular_sumatoria(datos)
    n = len(datos)
    if n == 0:
        return None  
    media = suma / n
    return media


def calcular_mediana(datos):
    datos_ordenados = ordenar_lista(datos)
    n = len(datos_ordenados)
    if n % 2 == 1:
        mediana = datos_ordenados[n // 2]
    else:
        mediana = (datos_ordenados[n // 2 - 1] + datos_ordenados[n // 2]) / 2
    return mediana


def calcular_moda(datos):
    frecuencias = {}
    for dato in datos:
        if dato in frecuencias:
            frecuencias[dato] += 1
        else:
            frecuencias[dato] = 1
    
    moda = []
    max_frecuencia = max(frecuencias.values())
    
    for dato, frecuencia in frecuencias.items():
        if frecuencia == max_frecuencia:
            moda.append(dato)
    
    return moda

def calcular_desviacion_estandar(datos):
    media = calcular_media(datos)
    n = len(datos)
    if n == 0:
        return None  
    
    suma_cuadrados_diferencia = 0
    for dato in datos:
        suma_cuadrados_diferencia += (dato - media) ** 2
    
    desviacion_estandar = (suma_cuadrados_diferencia / n) ** 0.5
    return desviacion_estandar

datos = ingresar_datos()
print("Datos ingresados:", datos)
print("Datos ordenados:", ordenar_lista(datos))
print("Sumatoria:", calcular_sumatoria(datos))
print("Media:", calcular_media(datos))
print("Mediana:", calcular_mediana(datos))
print("Moda:", calcular_moda(datos))
print("Desviación estándar:", calcular_desviacion_estandar(datos))