#Codigo base perteneciente a José Jezarel Sánchez Mijares
#Modificado por Antonio Silva Martínez
import matplotlib.pyplot as plt
import numpy as np
import cv2

def border(img,kernel,w_size=3):
  #seleccionamos el pivote
  wp=int((w_size-1)/3) 
  #Creacion de coordenadas donde tienen la longitud de las filas y columnas de la imagen
  l_x, l_y = img.shape[0], img.shape[1]
  #Hacemos un array de ceros donde iremos rellenando la imagen con blur
  border_img = np.zeros((l_x,l_y))
  #Recorrido de pixeles
  for i in range(wp,l_x-wp):
    for j in range(wp,l_y-wp):
      #vamos vacienado el promedio para cada punto
      suma = 0
      for m in range (-wp,wp+1):
        for l in range (-wp,wp+1):
          suma = suma + img[i+m,j+l]*kernel[m][l]
      border_img[i,j] =suma
  return border_img

# Cargar 10 imágenes locales
img_paths = ["C:/Users/ansm3/Desktop/python/Imagenes_stop/stop/imagen1.png",
             "C:/Users/ansm3/Desktop/python/Imagenes_stop/stop/imagen2.png",
             "C:/Users/ansm3/Desktop/python/Imagenes_stop/stop/imagen3.png",
             "C:/Users/ansm3/Desktop/python/Imagenes_stop/stop/imagen4.png",
             "C:/Users/ansm3/Desktop/python/Imagenes_stop/stop/imagen5.png",
             "C:/Users/ansm3/Desktop/python/Imagenes_stop/stop/imagen6.png",
             "C:/Users/ansm3/Desktop/python/Imagenes_stop/stop/imagen7.png",
             "C:/Users/ansm3/Desktop/python/Imagenes_stop/stop/imagen8.png",
             "C:/Users/ansm3/Desktop/python/Imagenes_stop/stop/imagen9.png",
             "C:/Users/ansm3/Desktop/python/Imagenes_stop/stop/imagen10.png"]

fig, axs = plt.subplots(2, 5, figsize=(20, 8))

for i, img_path in enumerate(img_paths):
  img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
  kernel1= np.array(([-1, 0, 1],
             [-2, 0, 2], 
             [-1, 0, 1]))
  border_image = border(img, kernel1, w_size=3)
  axs[i//5, i%5].imshow(border_image, cmap="gray")
  axs[i//5, i%5].set_title('Imagen {}'.format(i+1))

plt.show()

