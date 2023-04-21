import os
import cv2

# Ruta de la carpeta que contiene las imágenes
Color = 'C:/Users/ansm3/Desktop/python/Imagenes_stop/stop/'
Blanco_negro  = 'C:/Users/ansm3/Desktop/python/Imagenes_stop/imagenes_BN/'
Binario = 'C:/Users/ansm3/Desktop/python/Imagenes_stop/Binario/'
Binario_color = 'C:/Users/ansm3/Desktop/python/Imagenes_stop/Binario_color/'
Gaussiano = 'C:/Users/ansm3/Desktop/python/Imagenes_stop/Gaussiano/'

#Blanco y negro
def convertir_a_bn(ruta_color, ruta_bn):
    archivos_carpeta = os.listdir(ruta_color)
    nombres_imagenes = []
    numero_cambios_color = 1

    # Iteramos sobre cada archivo y agregamos solo los archivos de imagen a la lista
    for archivo in archivos_carpeta:
        # Comprobamos si el archivo tiene una extensión de imagen válida
        if archivo.endswith('.jpg') or archivo.endswith('.jpeg') or archivo.endswith('.png'):
            # Agregamos el nombre del archivo a la lista de nombres de imágenes
            nombres_imagenes.append(archivo)

    # Iteramos sobre cada imagen
    for nombre_imagen in nombres_imagenes:
        # Creamos la ruta completa del archivo de imagen
        ruta_imagen = os.path.join(ruta_color, nombre_imagen)
        imagen_color = cv2.imread(ruta_imagen) 
        # Convertimos la imagen a escala de grises
        imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)
        nuevo_nombre_archivo = f"_{numero_cambios_color}_bn.png"
        nuevo_nombre_archivo = archivo.split('.')[0] + nuevo_nombre_archivo
        ruta_archivo_modificado = os.path.join(ruta_bn, nuevo_nombre_archivo)
        # Guardamos la imagen en escala de grises
        cv2.imwrite(ruta_archivo_modificado, imagen_gris)
        numero_cambios_color += 1

#Binarización
def binarizar_imagenes(ruta_bn, ruta_binario, umbral=100):
    # Obtener la lista de archivos de la carpeta
    archivos_carpeta_bn = os.listdir(ruta_bn)
    nombres_imagenes_bn = []
    numero_cambios_bn = 1

    # Binarización de las imágenes
    for archivo_bn in archivos_carpeta_bn:
        # Comprobamos si el archivo tiene una extensión de imagen válida
        if archivo_bn.endswith('.jpg') or archivo_bn.endswith('.jpeg') or archivo_bn.endswith('.png'):
            # Agregamos el nombre del archivo a la lista de nombres de imágenes
            nombres_imagenes_bn.append(archivo_bn)
            
    for imagenes_bn in nombres_imagenes_bn:
       # Creamos la ruta completa del archivo de imagen
        ruta_imagen_bn = os.path.join(ruta_bn, imagenes_bn)
        imagen_bn = cv2.imread(ruta_imagen_bn)
        # Aplicar umbralización
        umbralizado_v0 = cv2.threshold(imagen_bn, umbral, 255, cv2.THRESH_BINARY)[1]
        nombre_archivo_bn = os.path.splitext(imagenes_bn)[0]
        nuevo_nombre_archivo_bn = f"{nombre_archivo_bn}_{numero_cambios_bn}_binario.bmp"
        ruta_archivo_modificado_blanco = os.path.join(ruta_binario, nuevo_nombre_archivo_bn)
        # Guardamos la imagen binarizada
        cv2.imwrite(ruta_archivo_modificado_blanco, umbralizado_v0)
        numero_cambios_bn += 1

# Binarización de las imágenes a color
def binarizar_imagenes_color(ruta_color, ruta_binario_color, umbral=127):
    # Obtener la lista de archivos de la carpeta
    archivos_carpeta_binario_color = os.listdir(ruta_color)
    nombres_imagenes_binario_color = []
    numero_cambios_binario_color = 1
    # Binarización de las imágenes
    for archivo_binario_color in archivos_carpeta_binario_color:
        # Comprobamos si el archivo tiene una extensión de imagen válida
        if archivo_binario_color.endswith('.jpg') or archivo_binario_color.endswith('.jpeg') or archivo_binario_color.endswith('.png'):
            # Agregamos el nombre del archivo a la lista de nombres de imágenes
            nombres_imagenes_binario_color.append(archivo_binario_color)    

    for imagenes_binario_color in nombres_imagenes_binario_color:
       # Creamos la ruta completa del archivo de imagen
        ruta_imagen_binario_color = os.path.join(ruta_color, imagenes_binario_color)
        imagen_binario_color = cv2.imread(ruta_imagen_binario_color)
        # Aplicar umbralización
        umbralizado = cv2.threshold(imagen_binario_color[:,:,1], umbral, 255, cv2.THRESH_BINARY)[1]
        nombre_archivo_bn = os.path.splitext(imagenes_binario_color)[0]
        nuevo_nombre_archivo_col = f"{nombre_archivo_bn}_{numero_cambios_binario_color}_bincol.png"
        ruta_archivo_modificado_blanco = os.path.join(ruta_binario_color, nuevo_nombre_archivo_col)
        # Guardamos la imagen binarizada
        cv2.imwrite(ruta_archivo_modificado_blanco, umbralizado)
        numero_cambios_binario_color += 1        


def ruido_gaussiano(Blanco_negro, Gaussiano):
    # Obtener la lista de archivos de la carpeta
    archivos_carpeta_Gaussiano = os.listdir(Blanco_negro)
    nombres_imagenes_gaussiano = []
    numero_cambios_gaussiano = 1
        # Binarización de las imágenes
    for archivo_gaussiano in archivos_carpeta_Gaussiano:
        # Comprobamos si el archivo tiene una extensión de imagen válida
        if archivo_gaussiano.endswith('.jpg') or archivo_gaussiano.endswith('.jpeg') or archivo_gaussiano.endswith('.png'):
            # Agregamos el nombre del archivo a la lista de nombres de imágenes
            nombres_imagenes_gaussiano.append(archivo_gaussiano)  

    for imagenes_gaussiano in nombres_imagenes_gaussiano:
       # Creamos la ruta completa del archivo de imagen
        ruta_imagen_gaussiano = os.path.join(Blanco_negro, imagenes_gaussiano)
        imagen_gaussiano = cv2.imread(ruta_imagen_gaussiano) 
        ##Incertar ruido gaussiano
        imagen_gaussiano_ruido = cv2.GaussianBlur(imagen_gaussiano, (0, 0), 10)
        nombre_archivo_gaussiano = os.path.splitext(imagenes_gaussiano)[0]
        nuevo_nombre_archivo_col = f"{nombre_archivo_gaussiano}_{numero_cambios_gaussiano}_gauss.png"
        ruta_imagen_gaussiano_ruido = os.path.join(Gaussiano, nuevo_nombre_archivo_col)
        cv2.imwrite(ruta_imagen_gaussiano_ruido, imagen_gaussiano_ruido)
        numero_cambios_gaussiano += 1        


convertir_a_bn(Color, Blanco_negro)
binarizar_imagenes(Blanco_negro, Binario)
binarizar_imagenes_color(Color, Binario_color)
ruido_gaussiano(Blanco_negro, Gaussiano)
