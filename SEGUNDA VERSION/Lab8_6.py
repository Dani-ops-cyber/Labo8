import cv2

# Inicializar la webcam
captura = cv2.VideoCapture(0)

if not captura.isOpened():
    print("No se puede acceder a la cámara")
    exit()

while True:
    # Leer un cuadro de la cámara
    ret, cuadro = captura.read()
    if not ret:
        print("No se puede recibir imagen (finalizando...)")
        break

    # Convertir el cuadro a escala de grises
    gris = cv2.cvtColor(cuadro, cv2.COLOR_BGR2GRAY)

    # Aplicar desenfoque para reducir el ruido
    desenfocado = cv2.GaussianBlur(gris, (5, 5), 0)

    # Detectar bordes usando Canny
    bordes = cv2.Canny(desenfocado, 50, 150)

    # Encontrar contornos en los bordes detectados
    contornos, _ = cv2.findContours(bordes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar los contornos en el cuadro original
    cv2.drawContours(cuadro, contornos, -1, (0, 255, 0), 2)

    # Mostrar el cuadro con los contornos detectados
    cv2.imshow('Contornos en tiempo real', cuadro)

    # Salir del bucle al presionar la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
captura.release()
cv2.destroyAllWindows()
