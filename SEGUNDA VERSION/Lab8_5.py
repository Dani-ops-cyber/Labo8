import cv2
import numpy as np

# Cargar la imagen en escala de grises
imagen = cv2.imread('/home/mario/Documentos/Embebidos/descarga.png', cv2.IMREAD_GRAYSCALE)

# Aplicar desenfoque para reducir el ruido
imagen_desenfocada = cv2.GaussianBlur(imagen, (5, 5), 0)

# Detectar bordes usando el algoritmo de Canny
bordes = cv2.Canny(imagen_desenfocada, 50, 150)

# Encontrar contornos en la imagen
contornos, _ = cv2.findContours(bordes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Convertir la imagen original a color para visualizar los contornos en color
imagen_contornos = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)

# Dibujar los contornos en la imagen
cv2.drawContours(imagen_contornos, contornos, -1, (0, 255, 0), 2)

# Mostrar la imagen con los contornos detectados
cv2.imshow("Contornos detectados", imagen_contornos)
cv2.waitKey(0)
cv2.destroyAllWindows()
